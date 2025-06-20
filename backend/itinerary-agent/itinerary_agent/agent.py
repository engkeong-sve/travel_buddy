"""
Agent module for managing itinerary generation using Google ADK tools.
"""
import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai import types
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from . import prompt
from .sub_agents.flight_agent.agent import flight_agent
from .sub_agents.hotel_agent.agent import hotel_agent
from .sub_agents.attraction_spot_agent.agent import attraction_spot_agent
from .sub_agents.restaurant_agent.agent import restaurant_agent
from .sub_agents.routing_agent.agent import routing_agent
from .sub_agents.template_agent.agent import template_agent
from .sub_agents.weather_agent.agent import weather_agent
from .sub_agents.packing_agent.agent import packing_agent
from .tools.tools import send_email, add_user_reminder_item, remove_user_reminder_item, \
    get_user_reminder_list


load_dotenv()  # load .env file
session_service = InMemorySessionService()

config = types.GenerateContentConfig(
    temperature=float(os.getenv('LLM_TEMPERATURE', 0.7)),
)

root_agent = Agent(
    name="manager",
    model=os.getenv('LLM_MODEL'),
    description="Creates a travel itinerary based on user preferences",
    generate_content_config=config,
    instruction=prompt.MANAGER_AGENT_PROMPT,
    tools=[
        AgentTool(hotel_agent),
        AgentTool(flight_agent),
        AgentTool(attraction_spot_agent),
        AgentTool(restaurant_agent),
        AgentTool(routing_agent),
        AgentTool(template_agent),
        AgentTool(weather_agent),
        AgentTool(packing_agent),
        send_email,
        add_user_reminder_item,
        remove_user_reminder_item,
        get_user_reminder_list,
    ],
)

runner = Runner(
    agent=root_agent, 
    app_name="itinerary_agent",
    session_service=session_service
)
