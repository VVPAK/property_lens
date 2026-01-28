"use client";

import { useState, useEffect, useRef } from "react";
import { Send, Bot, User, Loader2, Sparkles } from "lucide-react";
import ReactMarkdown from "react-markdown";
import clsx from "clsx";
import styles from "./Chat.module.css";

type Message = {
    role: "user" | "assistant";
    content: string;
};

const SUGGESTIONS = [
    {
        title: "Market Trends",
        desc: "Dubai Marina prices this month",
        query: "What are the current market trends in Dubai Marina? Show me price per sqft changes."
    },
    {
        title: "Calculate ROI",
        desc: "1BR in JVC (800k AED)",
        query: "Calculate ROI for a 1BR in JVC costing 800k AED with 65k rent."
    },
    {
        title: "Find Deals",
        desc: "Undervalued in Business Bay",
        query: "Find undervalued 1BR apartments in Business Bay under 1.2M AED."
    },
    {
        title: "Buying Process",
        desc: "Guide for non-residents",
        query: "Explain the property buying process for non-resident investors in Dubai."
    }
];

export default function Chat() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isLoading]);

    const handleSend = async (text: string) => {
        if (!text.trim() || isLoading) return;

        const userMessage: Message = { role: "user", content: text };
        setMessages((prev) => [...prev, userMessage]);
        setInput("");
        setIsLoading(true);

        try {
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/v1/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage.content }),
            });

            if (!res.ok) {
                throw new Error(await res.text() || "Failed to fetch response");
            }

            const data = await res.json();
            const aiMessage: Message = { role: "assistant", content: data.response };
            setMessages((prev) => [...prev, aiMessage]);
        } catch (error) {
            setMessages((prev) => [
                ...prev,
                { role: "assistant", content: `❌ **Connection Error**: ${error instanceof Error ? error.message : "Service unavailable"}.` }
            ]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div className={styles.brand}>
                    <div className="w-8 h-8 bg-black text-white rounded-lg flex items-center justify-center">
                        <Sparkles size={18} />
                    </div>
                    <h1 className={styles.title}>Property Lens</h1>
                </div>
            </header>

            <div className={styles.messages}>
                {messages.length === 0 ? (
                    <div className={styles.emptyState}>
                        <div className="bg-gray-100 p-4 rounded-2xl mb-4">
                            <Bot size={48} className="text-gray-400" />
                        </div>
                        <div>
                            <h2 className={styles.emptyTitle}>What's your investment goal?</h2>
                            <p className={styles.emptySubtitle}>
                                Real-time market analysis and ROI calculations.
                            </p>
                        </div>

                        <div className={styles.suggestionsGrid}>
                            {SUGGESTIONS.map((s, i) => (
                                <button
                                    key={i}
                                    className={styles.suggestionCard}
                                    onClick={() => handleSend(s.query)}
                                >
                                    <span className={styles.suggestionTitle}>{s.title}</span>
                                    <span className={styles.suggestionDesc}>{s.desc}</span>
                                </button>
                            ))}
                        </div>
                    </div>
                ) : (
                    <>
                        {messages.map((msg, idx) => (
                            <div
                                key={idx}
                                className={clsx(
                                    styles.messageRow,
                                    msg.role === "user" ? styles.userRow : ""
                                )}
                            >
                                <div className={clsx(styles.avatar, msg.role === "user" ? styles.userAvatar : styles.aiAvatar)}>
                                    {msg.role === "user" ? <User size={18} /> : <Bot size={18} />}
                                </div>
                                <div className={clsx(styles.bubble, msg.role === "user" ? styles.userBubble : styles.aiBubble)}>
                                    <ReactMarkdown>{msg.content}</ReactMarkdown>
                                </div>
                            </div>
                        ))}
                        {isLoading && (
                            <div className={styles.messageRow}>
                                <div className={clsx(styles.avatar, styles.aiAvatar)}>
                                    <Bot size={18} />
                                </div>
                                <div className={styles.bubble}>
                                    <div className="flex items-center gap-2 text-gray-500">
                                        <Loader2 className="animate-spin w-4 h-4" />
                                        <span className="text-sm">Analyzing...</span>
                                    </div>
                                </div>
                            </div>
                        )}
                        <div ref={messagesEndRef} />
                    </>
                )}
            </div>

            <div className={styles.inputWrapper}>
                <div className={styles.inputContainer}>
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && handleSend(input)}
                        placeholder="Ask about prices, ROI, or market trends..."
                        className={styles.input}
                        disabled={isLoading}
                        autoFocus
                    />
                    <button
                        onClick={() => handleSend(input)}
                        disabled={isLoading || !input.trim()}
                        className={styles.sendButton}
                        aria-label="Send message"
                    >
                        {isLoading ? <Loader2 size={20} className="animate-spin" /> : <Send size={20} />}
                    </button>
                </div>
                <div className="text-center mt-2">
                    <p className="text-xs text-slate-400">AI generated. Verify financial data.</p>
                </div>
            </div>
        </div>
    );
}
