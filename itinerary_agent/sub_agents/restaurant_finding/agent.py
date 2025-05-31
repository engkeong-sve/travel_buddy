from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




restaurant_finding = Agent(
    name="restaurant_finding",
    model="gemini-2.0-flash",
    description="Restaurant Finding Agent",
    instruction=prompt.RESTAURANT_FINDING_PROMPT,
    tools = [google_search],
)
