
"""Agent module for searching available flights based on user queries."""

from google.adk import Agent
from google.adk.tools import google_search
import datetime
from .tools import search_flight

MODEL = "gemini-2.0-flash"

# root_agent = Agent(
#     model=MODEL,
#     name="flight_agent",
#     instruction=prompt.flight_agent_instruction(),
#     output_key="available_flights",
#     description="Flight agent for searching available flights based on user queries.",
#     tools=[google_search],
# )


root_agent = Agent(
    name="flight_search_agent",
    model=MODEL,
    description="Flight search agent for finding available flights based on user queries.",
    instruction=f"""You are a helpful travel assistant who can help to check on the exact flight for the user.
    You can check with users if the details are not sufficient to find a flight.
    You must strictly follow the Key Constraints and Output Format provided below.
    
    Today's date is {datetime.datetime.now()}.
    When performing flight searching, please ensure that the dates are in future, not the past.
    
    You can use the following tools:
    - search_flight: Search for flights based on user criteria using the Google Flights API.
    
    **Key Constraints**:
    - Response flights information with Output Format.
    
    **Output Format**:
        - Airlines
        - Flight number (with url if available)
        - Origin city or airport
        - Destination city or airport
        - Departure date and time (duration in hours)
        - Connection details (if applicable)
        - Return date and time (duration in hours, if applicable)
        - Class of service (e.g., Economy, Business)
        - Number of passengers (e.g., adults, children)
        - Price (breakdown by adults and children)
        - Total cost
    """,
    tools=[search_flight]
)
