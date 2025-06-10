
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types

from . import prompt


config = types.GenerateContentConfig(
    temperature=os.environ.get('LLM_TEMPERATURE', 0.7),
)

routing_agent = Agent(
    name="routing_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Search for optimal route agent",
    generate_content_config=config,
    instruction=prompt.ROUTING_AGENT_PROMPT,
    tools = [google_search],
)
