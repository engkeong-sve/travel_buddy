
import os
from serpapi import GoogleSearch
from google.adk.tools import ToolContext

def flight_search(
    departure_id: str,
    arrival_id: str,
    outbound_date: str,
    return_date: str,
    departure_currency: str,
    adult_count: int,
    child_count: int,
    tool_context: ToolContext,
) -> dict:
    """Search for flights using the Google Flights API.
    Args:
        departure_id (str): The IATA code for the departure airport.
        arrival_id (str): The IATA code for the arrival airport.
        outbound_date (str): The date of departure in YYYY-MM-DD format.
        return_date (str): The date of return in YYYY-MM-DD format, or None if one-way.
        departure_currency (str): The currency code for the flight prices.
        adult_count (int): The number of adults traveling.
        child_count (int): The number of children traveling.
        tool_context (ToolContext): Context object to store state and results.
    """
    params = {
        'api_key': os.environ.get('SERPAPI_API_KEY'),
        'engine': 'google_flights',
        'hl': 'en',
        'departure_id': departure_id,
        'arrival_id': arrival_id,
        'outbound_date': outbound_date,
        'return_date': return_date,
        'currency': departure_currency,
        'adults': adult_count,
        'children': child_count,
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        best_flights = results.get('best_flights', [])
        other_flights = results.get('other_flights', [])
        price_insights = results.get('price_insights', {})
        airports = results.get('airports', {})
        output = {
            'status': 'success',
            'best_flights': best_flights,
            'other_flights': other_flights,
            'price_insights': price_insights,
            'airports': airports,
        }
        tool_context.state['available_flights'] = output
        return output
    except Exception as e:
        return {
            'status': 'failed',
            'error_msg': e,
        }
        