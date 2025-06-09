
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt


attraction_spot_agent = Agent(
    name="attraction_spot_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Search for top attraction spots agent",
    instruction=prompt.ATTRACTION_SPOT_PROMPT,
    tools = [google_search],
)
