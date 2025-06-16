
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types

from . import prompt


config = types.GenerateContentConfig(
    temperature=os.environ.get('LLM_TEMPERATURE', 0.7),
)

packing_agent = Agent(
    name="packing_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Generates a list of items to be packed for traveling",
    generate_content_config=config,
    instruction=prompt.PACKING_AGENT_PROMPT,
    tools = [google_search],
)
