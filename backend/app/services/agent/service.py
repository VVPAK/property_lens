from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from app.core.config import settings
from app.services.agent.tools import SearchPropertiesTool, ROICalculatorTool

class AgentService:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=0
        )
        self.tools = [SearchPropertiesTool(), ROICalculatorTool()]
        
        # Create a prebuilt ReAct agent using LangGraph
        self.agent = create_react_agent(self.llm, self.tools)

    async def chat(self, user_input: str):
        """
        Run the agent with the user input (Standard).
        """
        inputs = {"messages": [HumanMessage(content=user_input)]}
        response = await self.agent.ainvoke(inputs)
        return response["messages"][-1].content

    async def chat_stream(self, message: str):
        """
        Process a message and yield chunks (Streaming).
        """
        try:
            # astream_events allows us to see intermediate steps if needed.
            inputs = {"messages": [HumanMessage(content=message)]}
            async for event in self.agent.astream_events(inputs, version="v1"):
                kind = event["event"]
                # Stream content from the final LLM response (on_chat_model_stream)
                if kind == "on_chat_model_stream" and "chunk" in event["data"]:
                    content = event["data"]["chunk"].content
                    if content:
                        yield content
        except Exception as e:
            yield f"Error: {str(e)}"

agent_service = AgentService()
