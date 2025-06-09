
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt


routing_agent = Agent(
    name="routing_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Search for optimal route agent",
    instruction=prompt.ROUTING_AGENT_PROMPT,
    tools = [google_search],
)
