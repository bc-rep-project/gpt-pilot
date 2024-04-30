from langchain.agents import Tool, ZeroShotAgent, AgentExecutor
from langchain_community.utilities import SerpAPIWrapper
from helpers.langchain_wrapper import LangChainLLMWrapper

class ResearchAgent:
    def __init__(self, llm_wrapper: LangChainLLMWrapper):
        self.llm_wrapper = llm_wrapper
        self.tools = [
            Tool(
                name="Search",
                func=SerpAPIWrapper().run,
                description="useful for when you need to answer questions about current events or find information",
            )
        ]

    def research(self, query: str) -> str:
        # You can customize the objective based on the specific research needs
        objective = f"Research the following: {query}" 
        return self.llm_wrapper.use_tools(objective, self.tools)