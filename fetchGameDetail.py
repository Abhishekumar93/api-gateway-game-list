"""
Lambda function to fetch game details using API Gateway path parameters.
"""
import os
import json
import requests

def lambda_handler(event, context):
    """
    Fetches game details from RAWG API based on the dynamic path parameter `{game_slug}`.
    """
    api_key = os.environ.get("RAWG_API_KEY")  # Use environment variable for security
    base_url = "https://api.rawg.io/api/games"

    # Get game_slug from API Gateway path parameters
    game_slug = event.get("pathParameters", {}).get("game_slug")
    # Validate input
    if not game_slug:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": "Missing required path parameter: game_slug"})
        }

    # Construct API URL
    url = f"{base_url}/{game_slug}?key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises error for 4xx/5xx responses

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(response.json())  # Ensure response is serialized properly
        }

    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": str(e)})
        }


"""
API to hit lambda function created in API Gateway
https://mo5i6a95m9.execute-api.us-east-1.amazonaws.com/prod/<game_slug>
"""