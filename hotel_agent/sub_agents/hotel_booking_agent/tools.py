# move the serpapi to here
from google.adk.tools import ToolContext
import datetime

def book_hotel(hotel_name: str, tool_context: ToolContext):
    """
    Perform hotel booking based on the top 5 hotels from search_hotel.
    """
    # update state 
    current_time = datetime.datetime.now()
    
    # current_hotel_booking = tool_context.state.get("hotel_booking_list",[])

    booking_detail = {
        'booking_date': str(current_time),
        'hotel': hotel_name,
    }

    # add the new hotel booking into current_hotel_booking
    
    tool_context.state['hotel_booking_list'] = booking_detail
    
    return {
        "status": "success",
        "message": "Successfully booked Hotel",
    }