import json
import requests
from datetime import datetime


def get_current_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

tools = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False
        },
        "strict": True
    }
}]












"""
functions = [
    {
            "name": "get_current_weather",
            "description": "Get current temperature for provided coordinates.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
               },
               "temperature_unit": {"type": "string", "enum": ["celsius", "fahrenheit"],
               "description": "The unit of measurement for temperature."
                }

            },
            "required": ["latitude", "longitude"],

    }

]
"""

# How do we make a function definition for Tavily?


'''

# we should be able to chain these functions together if we use LCEL

# this takes in the latest message in the chat_log and returns it as the query
def tavily_get_input(chat_log):
    query = chat_log[-1]
    return query


# this takes in the query and returns the search result
def tavily_search(query):
    search_result = tavily_client.search(query, max_results=1, topic="general", search_depth="basic", max_tokens=5000)
    return search_result

# now what do we do with the search result?

chat_log.append({'role': 'assistant', 'content': search_result})
chat_responses.append(search_result)

'''