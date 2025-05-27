from google.adk.agents import Agent
from .tools import cancel_hotel_booking
# from .tools import modify_hotel_details
import datetime



hotel_cancellation_agent = Agent(
    name='hotel_cancellation_agent',
    model='gemini-2.0-flash',
    description='Hotel cancellation agent',
    instruction='''
    You are a helpful hotel cancellation agent who is able to help user to process the cancellation of a hotel.

    Below is the details of the user's current booking.
    Hotel Booking Details
    {hotel_booking_list}

    If there is no hotel booked by the user, and the user intends to book a hotel, delegate to hotel booking agent.
    
    Else, if the user has a booking, use the following tools according to the user's requests:
    - cancel_hotel_booking
    - modify_hotel_details
    ''',
    tools=[cancel_hotel_booking], #, modify_hotel_details],
)