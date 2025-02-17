#Kypton Lantz
#February 17, 2025
#Module 9 - Assignment 2: APIs
#
#This program connect to an API and print the retrieved data both with and without formatting.

import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

try:
    response = requests.get("https://anapioficeandfire.com/api/characters/583")
    print("Connection Status code:")
    print(response.status_code)
    
    print("\nUnformatted data:")
    print(response.json())

    print("\nFormatted data:")
    jprint(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection error occurred: {e}")