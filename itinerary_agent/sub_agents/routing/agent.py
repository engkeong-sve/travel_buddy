from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




routing = Agent(
    name="routing",
    model="gemini-2.0-flash",
    description="Routing Agent",
    instruction=prompt.ROUTING_AGENT_PROMPT,
    tools = [google_search],
)
