
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt


weather_agent = Agent(
    name="weather_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Weather Agent",
    instruction=prompt.WEATHER_AGENT_PROMPT,
    tools = [google_search],
)
