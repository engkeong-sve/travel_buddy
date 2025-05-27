from google.adk.tools import ToolContext
import datetime

def cancel_hotel_booking(tool_context: ToolContext):
    """
    Performs hotel booking cancellation based on the hotel that has been booked.
    """

    current_time = datetime.datetime.now()

    tool_context.state['hotel_booking_list'] = {}
    
    return {
        "status": "success",
        "message": "Successfully removed Hotel booking",
        "hotel_details": "",
        "timestamp": current_time,
    }

# def modify_hotel_details(tool_context: ToolContext):
#     """
#     Performs hotel booking modification based on the hotel that has been booked.
#     """

#     current_time = datetime.datetime.now()
    
#     current_hotel_booking = tool_context.state.get("hotel_booking_list",[])

#     # add the new hotel booking into current_hotel_booking
#     remove_hotel_booking = current_hotel_booking.remove("Hotel book")

#     tool_context.state['hotel_booking_list'] = remove_hotel_booking
    
#     return {
#         "status": "success",
#         "message": "Successfully removed Hotel booking",
#         "hotel_details": "",
#         "timestamp": current_time,
#     }

# consider to add hotel modification agent