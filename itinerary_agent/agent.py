"""
Agent module for managing itinerary generation using Google ADK tools.
"""
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.flight_agent.agent import flight_agent
from .sub_agents.hotel_agent.agent import hotel_agent
from .sub_agents.attraction_spot_agent.agent import attraction_spot_agent
from .sub_agents.restaurant_agent.agent import restaurant_agent
from .sub_agents.routing_agent.agent import routing_agent
from .sub_agents.template_agent.agent import template_agent
from .sub_agents.weather_agent.agent import weather_agent
from .tools.tools import send_email, add_user_todo_item, remove_user_todo_item, \
    get_user_todo_list


root_agent = Agent(
    name="manager",
    model=os.environ.get('LLM_MODEL'),
    description="Creates a travel itinerary based on user preferences",
    instruction=prompt.MANAGER_AGENT_PROMPT,
    tools=[
        AgentTool(hotel_agent),
        AgentTool(flight_agent),
        AgentTool(attraction_spot_agent),
        AgentTool(restaurant_agent),
        AgentTool(routing_agent),
        AgentTool(template_agent),
        AgentTool(weather_agent),
        send_email,
        add_user_todo_item,
        remove_user_todo_item,
        get_user_todo_list,
    ],
)
