from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt


routing_agent = Agent(
    name="routing_agent",
    model="gemini-2.0-flash",
    description="Search for optimal route agent",
    instruction=prompt.ROUTING_AGENT_PROMPT,
    tools = [google_search],
)
