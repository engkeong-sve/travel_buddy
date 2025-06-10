
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types

from . import prompt


config = types.GenerateContentConfig(
    temperature=os.environ.get('LLM_TEMPERATURE', 0.7),
)

weather_agent = Agent(
    name="weather_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Weather Agent",
    generate_content_config=config,
    instruction=prompt.WEATHER_AGENT_PROMPT,
    tools = [google_search],
)
