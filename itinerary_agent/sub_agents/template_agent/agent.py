
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types
from dotenv import load_dotenv

from . import prompt


load_dotenv()  # load .env file

config = types.GenerateContentConfig(
    temperature=float(os.getenv('LLM_TEMPERATURE', 0.7)),
)


template_agent = Agent(
    name="template_agent",
    model=os.getenv('LLM_MODEL'),
    description="Find available travel template online agent",
    generate_content_config=config,
    instruction=prompt.TEMPLATE_AGENT_PROMPT,
    tools = [google_search],
)
