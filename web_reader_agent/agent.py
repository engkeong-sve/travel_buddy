"""Web Reader Agent"""

from google.adk import Agent
from google.adk.tools import google_search
from google.genai import types

from .tools.web_loader import web_loader

MODEL = "gemini-2.0-flash"

# config = types.GenerateContentConfig(
#     temperature=0.3,
# )

prompt = """You are expert in reading web content and extracting information from HTML documents.
You have access to a web loader tool that can retrieve HTML content from a given URL.
Whenever user provide you an URL, you will use the web loader tool to fetch the HTML content.
Your task is to read the HTML content and extract information.
You will follow these rules:
    - ONLY load 1 URL at a time.
    - DO NOT summarize or interpret the content, just extract the information as it is.
    - Ignore any advertisements or irrelevant content.
    - Retain the structure of tables in table format.
    - ONLY return extracted information in the response, no additional text.
"""

root_agent = Agent(
    model=MODEL,
    name="web_reader_agent",
    instruction=prompt,
    # generate_content_config=config,
    output_key="web_content",
    description="Agent to read web content by URL",
    tools=[web_loader],
)
