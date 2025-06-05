from google.adk import Agent
from .tools import book_hotel


hotel_booking_agent = Agent(
    name='hotel_booking_agent',
    model='gemini-2.0-flash',
    description='Hotel booking agent',
    instruction='''
    You are a helpful hotel booking agent that is able to secure the hotel room(s) according to the user's preference.

    Below are the top 5 hotel details that the user is given with.
    Hotel details: 
    {hotel_search_list}

    If the user chooses a hotel to book, you may use the tool to perform hotel booking.
    - book_hotel
    ''',
    tools=[book_hotel],
)