#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step by step instructions can be found in the appendix A of this assignment brief. 
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by stepdevelopment process. 

# =========================
# REQUIRED LIBRARIES
# =========================

import requests
import json
import time
import os # import os module to access environment variables
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

global use_hardcoded_key
use_hardcoded_key = False # Default to use False (During Testing True)
api_keys_used = ("weather_api", "webex_api", "ISS_api", "Geocoding_api")
api_keys_hardcoded = {
    "weather_api": "provide_key",
    "webex_api": "provide_key",
    "ISS_api": "provide_key",
    "Geocoding_api": "provide_key"
}
# =========================
# CONFIGURATION FUNCTIONS
# =========================
#if system defined keys exist use those else if harcoded keys exist in the python file exist use those else use user provided keys 

def get_api_keys(api_keys_used, use_hardcoded_key, api_keys_hardcoded):
    api_keys = {}
    for key_name in api_keys_used:
        env_var_name = f"{key_name}_key"
        api_key = os.getenv(env_var_name)
        if not api_key:
            print(f"Error: {env_var_name} not found in environment variables. using hardcoded key instead.")
            if use_hardcoded_key:
                api_key = api_keys_hardcoded.get(key_name)
            else:
                api_key = str(input(f"Provide API Key for api: {key_name}: "))
        api_keys[key_name] = api_key
    return api_keys # api_keys is a dictionary containing api_keys, example: {"weather_api": "your_weather_api_key", "webex_api": "your_webex_api_key", ...}

#def get_webex_token():
#    choice = input("Use hard-coded Webex token? (y/n): ").lower()
#    if choice == "n":
#        token = input("Enter your Webex Access Token: ")
#        return f"Bearer {token}"
#    else:
#        return "Bearer NWZmMWJhZDUtMWVjYi00Mzg2LWJlYzMtNWQ1ZGUxZmE1Yjc4YmIwMTY1NTctNWI2_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17"

# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = "https://webexapis.com/v1/rooms"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(
            url,
        headers=headers,
        timeout=10,
    )

    if response.status_code != 200:
        print("Error fetching rooms:", response.status_code)
        return []

    return response.json().get("items", [])


def print_rooms(rooms):
    for room in rooms:
        print(f"Room: {room['title']}, ID: {room['id']}")


def select_room(rooms):
    while True:
        name = input("Enter the room name: ")
        for room in rooms:
            if name.lower() in room["title"].lower():
                print(f"Selected room: {room['title']}")
                return room["id"]
        print("Room not found. Please try again.")


def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId":{room_id}, "max": 100}
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None, None

    data = response.json().get("items", [])

    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")

def send_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "roomId": room_id,
        "text": message
    }
    response = requests.request('POST', url, headers=headers, data = JSON.dumps(data))

    if response.status_code != 200:
        print("Error sending message:", response.status_code, response.text)

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"city":{city}, "appid": api_key} 
    response = requests.request('GET', url, parameters=params,)


    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        return "Location was not found"
    first_lat = location['lat']
    first_lon = location['lon']
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"lat": first_lat, "lon": first_lon, "appid": api_key}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Error fetching weather data"

    weather = response.json()

    return (
        f"City: {weather['name']}, Country: {weather['sys']['country']}, "
        f"Temperature: {weather['main']['temp']}K, "
        f"Weather: {weather['weather'][0]['description']}, "
        f"Humidity: {weather['main']['humidity']}%, "
        f"Wind Speed: {weather['wind']['speed']} m/s"
    )

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = "http://api.openweathermap.org/geo/1.0/reverse"
    params = {
                "lat": lat,
                "lon": lon,
                "limit": 1, 
                "appid": api_key
            }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = location.get("name", "Over Ocean / No Nearby City")

    return (
        f"Latitude: {lat}, Longitude: {lon}, Place: {place}"
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main(api_keys_used, use_hardcoded_key, api_keys_hardcoded):
    
    api_keys = get_api_keys(api_keys_used, use_hardcoded_key, api_keys_hardcoded)
                  

    #token = get_webex_token()

    weather_key = api_keys.get("weather_api")
    token = api_keys.get("webex_api")
    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found.")
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print(f"Received message: {message_text}")

            if not message_text.startswith("/"):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith("/weather"):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "/iss":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "/quit":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)

print(os.getenv("weather_api_key"))
main(api_keys_used, use_hardcoded_key, api_keys_hardcoded)
