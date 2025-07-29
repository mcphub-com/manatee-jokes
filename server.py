import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Rufasa85/api/manatee-jokes'

mcp = FastMCP('manatee-jokes')

@mcp.tool()
def random() -> dict: 
    '''retrieves a random manatee joke'''
    url = 'https://manatee-jokes.p.rapidapi.com/manatees/random'
    headers = {'x-rapidapi-host': 'manatee-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''gets a specific joke by id'''
    url = 'https://manatee-jokes.p.rapidapi.com/manatees/%7Bid%7D'
    headers = {'x-rapidapi-host': 'manatee-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def find_all() -> dict: 
    '''retrieves all available jokes'''
    url = 'https://manatee-jokes.p.rapidapi.com/manatees'
    headers = {'x-rapidapi-host': 'manatee-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
