from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from app.core.config import settings
from app.services.agent.tools import SearchPropertiesTool, ROICalculatorTool

class AgentService:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o",
            temperature=0
        )
        self.tools = [SearchPropertiesTool(), ROICalculatorTool()]
        
        # Create a prebuilt ReAct agent using LangGraph
        self.agent = create_react_agent(self.llm, self.tools)

    async def chat(self, user_input: str):
        """
        Run the agent with the user input.
        """
        # LangGraph agents expect a list of messages
        inputs = {"messages": [HumanMessage(content=user_input)]}
        
        # Invoke the graph
        response = await self.agent.ainvoke(inputs)
        
        # The last message in the state is the AI's final response
        return response["messages"][-1].content

agent_service = AgentService()
