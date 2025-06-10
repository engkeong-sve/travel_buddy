
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types

from . import prompt


config = types.GenerateContentConfig(
    temperature=os.environ.get('LLM_TEMPERATURE', 0.7),
)

restaurant_agent = Agent(
    name="restaurant_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Search for restaurant agent",
    generate_content_config=config,
    instruction=prompt.RESTAURANT_AGENT_PROMPT,
    tools = [google_search],
)
