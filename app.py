# playground.py
from datetime import datetime
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.tavily import TavilyTools

current_year = datetime.now().year

web_search_agent = Agent(
    name="Web Search Agent",
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[TavilyTools(api_key="your_tavily_key")],
    instructions=[f"You are a real-time market research analyst.",
        f"Always process tool outputs to analyze data for the current year ({current_year}).",
        "Never refuse queries asking for current data when web search tools are enabled.",
        "Extract key findings directly from tool results and present them concisely."],
    show_tool_calls=True,
    markdown=False,
)

# Test execution directly in terminal
web_search_agent.print_response("What are the  Top 3 Trends sales in iraq today ?", stream=True)
