
"""Agent module for searching available flights based on user queries."""
import os
import datetime
from google.adk import Agent
from google.genai import types
from .tools import flight_search
from dotenv import load_dotenv

load_dotenv()  # load .env file

config = types.GenerateContentConfig(
    temperature=float(os.getenv('LLM_TEMPERATURE', 0.7)),
)

flight_agent = Agent(
    name="flight_agent",
    model=os.getenv('LLM_MODEL'),
    description="Flight agent for finding available flights based on user queries.",
    generate_content_config=config,
    instruction=f"""You are a helpful flight agent who can help to find available flights based on user queries.
    You can check with users if the details are not sufficient to find a flight.
    You MUST strictly follow the Key Constraints and Output Format provided below.
    
    These are available tools you can use:
    - flight_search: Search for flights based on user's criteria.
    
    **Key Constraints**:
    - Response flights information with Output Format.
    - Only return flights that are available and match the user's criteria.
    - When performing flight searching, please ensure that the dates are in future, not the past.
    
    **Output Format**:
        - Airlines
        - Flight number
        - Departure airport
        - Arrival airport
        - Departure date and time 
        - Duration (in hours)
        - Layovers (if applicable)
        - Return flight details (if applicable)
        - Class of service (e.g., Economy, Business)
        - Number of passengers (e.g., adults, children)
        - Price (breakdown by adults and children)
        - Total cost
    
    **Reference**:
    Today's date is {datetime.datetime.now()}.
    """,
    tools=[flight_search]
)
