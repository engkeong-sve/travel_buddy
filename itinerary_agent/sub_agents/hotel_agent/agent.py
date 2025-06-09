
import os
from google.adk import Agent
import datetime
from .tools import hotel_search


hotel_agent = Agent(
    name="hotel_agent",
    model=os.environ.get('LLM_MODEL'),
    description="Tool agent",
    instruction=f"""
    You are a helpful travel assistant who can help to check on the exact accommodation for the user.
    You can check with users if the details are not sufficient to find a hotel.

    Today's date is {datetime.datetime.now()}. 
    When performing hotel searching, please ensure that the dates are in future, not the past.
     
    You can use the following tools:
    - hotel_search
    """,
    tools=[hotel_search],
)
