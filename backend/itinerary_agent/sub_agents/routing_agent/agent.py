
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


routing_agent = Agent(
    name="routing_agent",
    model=os.getenv('LLM_MODEL'),
    description="Search for optimal route agent",
    generate_content_config=config,
    instruction=prompt.ROUTING_AGENT_PROMPT,
    tools = [google_search],
)
