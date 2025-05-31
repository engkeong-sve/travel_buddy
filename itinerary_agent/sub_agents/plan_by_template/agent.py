from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

from . import prompt




plan_by_template = Agent(
    name="plan_by_template",
    model="gemini-2.0-flash",
    description="Plan by Template Agent",
    instruction=prompt.PLAN_BY_TEMPLATE_PROMPT,
    tools = [google_search],
)
