from google.adk import Agent
from .tools import book_hotel

hotel_search_details = '''
Ananti at Busan Village: 5-star hotel with an overall rating of 4.8. The total rate for your stay would be $1,230 before taxes and fees.
UH Continental CenterPoint: Hotel with an overall rating of 4.9. The total rate for your stay would be $482 before taxes and fees.
Gwanganli Hotel 1: 2-star hotel with an overall rating of 4.7. The total rate for your stay would be $148 before taxes and fees.
Ananti Cove: 4-star hotel with an overall rating of 4.6. The total rate for your stay would be $1,023 before taxes and fees.
Park Hyatt Busan: 5-star hotel with an overall rating of 4.6. The total rate for your stay would be $693 before taxes and fees.
'''

hotel_booking_agent = Agent(
    name='hotel_booking_agent',
    model='gemini-2.0-flash',
    description='Hotel booking agent',
    instruction=f'''
    You are a helpful hotel booking agent that is able to secure the hotel room(s) according to the user's preference.

    Below are the top 5 hotel details that the user is given with.
    Hotel details: 
    {hotel_search_details}

    If the user chooses a hotel to book, you may use the tool to perform hotel booking.
    - book_hotel
    ''',
    tools=[book_hotel],
)