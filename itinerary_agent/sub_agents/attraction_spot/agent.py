from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




attraction_spot = Agent(
    name="attraction_spot",
    model="gemini-2.0-flash",
    description="Attraction Spot Agent",
    instruction=prompt.ATTRACTION_SPOT_PROMPT,
    tools = [google_search],
)
