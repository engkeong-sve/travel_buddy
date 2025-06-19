import os
from google.adk.tools import ToolContext
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv() 


def hotel_search(location: str, check_in_date: str, check_out_date: str,
                  adults: int, children: int, rooms: int, tool_context: ToolContext):
    '''
    Find hotels using the Google Hotels engine.
    
    Args:
        location (str): The location of the hotel.
        check_in_date (str): Check-in date. The format is YYYY-MM-DD. e.g. 2024-06-22
        check_out_date (str): Check-out date. The format is YYYY-MM-DD. e.g. 2024-06-28
        adults (int): Number of adults staying in the hotel, default as 2 if not specified.
        children (int): Number of children staying in the hotel, default as 0 if not specified.
        rooms (int): Number of rooms required, default as 1 if not specified.
        
    Returns:
        dict: Hotel search results.
    '''

    params = {
        'api_key': os.getenv('SERPAPI_API_KEY'),
        'engine': 'google_hotels',
        'hl': 'en',
        'gl': 'us',
        'q': location,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'currency': 'USD',
        'adults': adults,
        'children': children,
        'rooms': rooms,
        'sort_by': 8,
        'hotel_class': None,
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        tool_context.state["hotel_search_list"] = results['properties'][:5]
        return {
            'status': 'success',
            'hotel_list': results['properties'][:5],
        }
    except Exception as e:
        return {
                'status': 'failed',
                'error_msg': e,
            }
        