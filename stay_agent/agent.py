from google.adk.agents import Agent
from .sub_agents.hotel_booking_agent.agent import hotel_booking_agent
from .sub_agents.hotel_cancellation_agent.agent import hotel_cancellation_agent
from .sub_agents.hotel_search_agent.agent import hotel_search_agent

root_agent = Agent(
    name='root_agent',
    model='gemini-2.0-flash',
    description='Hotel service agent',
    instruction=f'''
    You are a hotel service agent.
    Your role is to help users with any query related to hotel, and direct them to respective specialized agent.

    Core Capabilities: direct user to the required subagent. 

    You have access to the following specialized agents:
    
    1. Hotel Search Agent
        - If user tells you to find a hotel, delegate to Hotel Search Agent.

    2. Hotel Booking Agent
        - If user wants to book a hotel, delegate to Hotel Booking Agent.

    3. Hotel Cancellation Agent 
        - If user wants to cancel a hotel, delegate to Hotel Cancellation Agent.
    ''',
    sub_agents=[hotel_search_agent, hotel_booking_agent, hotel_cancellation_agent],
)