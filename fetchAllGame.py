"""
This code is for fetching all the games by using lambda function and api gateway
"""
import json
import requests

#This is the lambda function to get the list of games. This function is also used for searching games

def lambda_handler(event, context):
  
    query = event['query'];
    
    page_size = page = search = ''
    
    if query:
        
        try:
            page_size = f"&page_size={query['page_size']}"
        except Exception as e:
            page_size = ''
        
        try:
            page = f"&page={query['page']}"
        except Exception as e:
            page = ''
        
        try:
            search = f"&search={query['search']}"
        except Exception as e:
            search = ''
    
    response = requests.get(f"https://api.rawg.io/api/games?key=e648abe0c449445c8b7373607e545a31{page_size}{page}{search}")
    
    return {
        'statusCode': response.status_code,
        'body': response.json()
    }


"""
API to hit lambda function created in API Gateway
https://mo5i6a95m9.execute-api.us-east-1.amazonaws.com/prod/games?search=<search_value>
"""