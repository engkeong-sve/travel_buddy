from google.adk import Agent
from dotenv import load_dotenv
import datetime
from .tools import search_hotel


hotel_search_agent = Agent(
    name="hotel_search_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction=f"""
    You are a helpful travel assistant who can help to check on the exact accommodation for the user.
    You can check with users if the details are not sufficient to find a hotel.

    Today's date is {datetime.datetime.now()}. 
    When performing hotel searching, please ensure that the dates are in future, not the past.
     
    You can use the following tools:
    - search_hotel

    """,
    tools=[search_hotel],
)