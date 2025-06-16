
import os
import datetime
from google.adk import Agent
from google.genai import types
from dotenv import load_dotenv
from .tools import hotel_search

load_dotenv()  # load .env file

config = types.GenerateContentConfig(
    temperature=float(os.getenv('LLM_TEMPERATURE', 0.7)),
)

hotel_agent = Agent(
    name="hotel_agent",
    model=os.getenv('LLM_MODEL'),
    description="Tool agent",
    generate_content_config=config,
    instruction=f"""
    You are a helpful travel assistant who can help to check on the exact accommodation for the user.
    You can check with users if the details are not sufficient to find a hotel.

    Today's date is {datetime.datetime.now()}. 
    When performing hotel searching, please ensure that the dates are in future, not the past.
     
    You can use the following tools:
    - hotel_search: Search for hotels based on user criteria using the Google Hotels API.

    **Key Constraints**:
    - Response hotel information with Output Format.
    
    **Output Format**:
        - Hotel name
        - Address
        - Check-in date and time
        - Check-out date and time
        - Number of rooms
        - Number of guests (adults, children)
        - Room type (e.g., single, double, suite)
        - Price per night (breakdown by adults and children)
        - Total cost for the stay
        - Booking URL (if available)
    """,
    tools=[hotel_search],
)
