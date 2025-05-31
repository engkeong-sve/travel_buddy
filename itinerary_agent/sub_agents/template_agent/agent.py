from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




template_agent = Agent(
    name="template_agent",
    model="gemini-2.0-flash",
    description="Find available travel template online agent",
    instruction=prompt.TEMPLATE_AGENT_PROMPT,
    tools = [google_search],
)
