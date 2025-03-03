import os
import json
import requests

def lambda_handler(event, context):
    """
    Fetches a list of games from RAWG API.
    Supports pagination and search queries.
    """
    rawg_api_key = os.environ.get('RAWG_API_KEY')  # Get API key from environment variables e648abe0c449445c8b7373607e545a31
    base_url = "https://api.rawg.io/api/games"
    
    # Use .get() to prevent KeyError
    query = event.get('query', {})  

    # Extract parameters safely
    page_size = query.get("page_size", "")
    page_size = f"&page_size={page_size}" if page_size else ""
    page = query.get("page", "")
    page = f"&page={page}" if page else ""
    search = query.get("search", "")
    search = f"&search={search}" if search else ""
    
    # Construct request URL
    url = f"{base_url}?key={rawg_api_key}{page_size}{page}{search}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for HTTP 4xx/5xx responses

        return {
            "statusCode": response.status_code,
            "body": response.json()
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

"""
API to hit lambda function created in API Gateway
https://khaldgbp54.execute-api.us-east-1.amazonaws.com/prod/games
"""