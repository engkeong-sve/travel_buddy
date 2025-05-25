
"""Agent module for searching available flights based on user queries."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.0-flash"

root_agent = Agent(
    model=MODEL,
    name="flight_agent",
    instruction=prompt.flight_agent_instruction(),
    output_key="available_flights",
    description="Flight agent for searching available flights based on user queries.",
    tools=[google_search],
)
