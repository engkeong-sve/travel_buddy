
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt


template_agent = Agent(
    name="template_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Find available travel template online agent",
    instruction=prompt.TEMPLATE_AGENT_PROMPT,
    tools = [google_search],
)
