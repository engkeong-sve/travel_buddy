from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




restaurant_agent = Agent(
    name="restaurant_agent",
    model="gemini-2.0-flash",
    description="Search for restaurant agent",
    instruction=prompt.RESTAURANT_AGENT_PROMPT,
    tools = [google_search],
)
