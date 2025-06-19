
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types

from .prompt import ATTRACTION_SPOT_PROMPT


config = types.GenerateContentConfig(
    temperature=os.environ.get('LLM_TEMPERATURE', 0.7),
)

attraction_spot_agent = Agent(
    name="attraction_spot_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Search for top attraction spots agent",
    generate_content_config=config,
    instruction=ATTRACTION_SPOT_PROMPT,
    tools = [google_search],
)
