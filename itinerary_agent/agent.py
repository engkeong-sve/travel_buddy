"""
Agent module for managing itinerary generation using Google ADK tools.
"""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.attraction_spot.agent import attraction_spot
from .sub_agents.restaurant_finding.agent import restaurant_finding
from .sub_agents.routing.agent import routing
from .sub_agents.plan_by_template.agent import plan_by_template
from .sub_agents.weather.agent import weather
from .tools.tools import send_email



# Itinerary Agent
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Creates a travel itinerary based on user preferences",
    instruction=prompt.MANAGER_AGENT_PROMPT,
    tools=[AgentTool(attraction_spot),
           AgentTool(restaurant_finding),
           AgentTool(routing),
           AgentTool(plan_by_template),
           AgentTool(weather),
           send_email],
)
