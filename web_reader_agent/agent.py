"""Web Reader Agent"""

from google.adk import Agent
from google.adk.tools import google_search
from google.genai import types

from .prompt import web_reader_instruction
from .tools.web_loader import web_loader

MODEL = "gemini-2.0-flash"

# config = types.GenerateContentConfig(
#     temperature=0.3,
# )

root_agent = Agent(
    model=MODEL,
    name="web_reader_agent",
    instruction=web_reader_instruction(),
    # generate_content_config=config,
    output_key="web_content",
    description="Agent to read web content by URL",
    tools=[web_loader],
)
