import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import Chat from "./Chat";
import "@testing-library/jest-dom";

// Mock fetch
global.fetch = jest.fn(() =>
    Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ response: "Hello from AI" }),
    })
) as jest.Mock;

// Mock react-markdown
jest.mock("react-markdown", () => (props: any) => {
    return <>{props.children}</>;
});

// Mock lucide-react
jest.mock("lucide-react", () => ({
    Send: () => <span>Send</span>,
    Bot: () => <span>Bot</span>,
    User: () => <span>User</span>,
    Loader2: () => <span>Loader2</span>,
    Sparkles: () => <span>Sparkles</span>,
}));

describe("Chat Component", () => {
    beforeEach(() => {
        (global.fetch as jest.Mock).mockClear();
    });

    it("renders empty state correctly", () => {
        render(<Chat />);
        expect(screen.getByText("What's your investment goal?")).toBeInTheDocument();
    });

    it("sends a message and displays user input", async () => {
        render(<Chat />);

        const input = screen.getByPlaceholderText(/Ask about prices/i);
        fireEvent.change(input, { target: { value: "Dubai Marina" } });
        fireEvent.keyDown(input, { key: "Enter", code: "Enter" });

        expect(await screen.findByText("Dubai Marina")).toBeInTheDocument();
        expect(global.fetch).toHaveBeenCalledTimes(1);
    });

    it("displays AI response", async () => {
        render(<Chat />);

        const input = screen.getByPlaceholderText(/Ask about prices/i);
        fireEvent.change(input, { target: { value: "Hello" } });

        const button = screen.getByRole("button", { name: /Send message/i });
        fireEvent.click(button);

        await waitFor(() => {
            expect(screen.getByText("Hello from AI")).toBeInTheDocument();
        });
    });
});
