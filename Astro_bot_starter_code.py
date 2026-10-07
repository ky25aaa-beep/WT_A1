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
from datetime import datetime
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

def handle_api_error(api_name, response, query, token=None, room_id=None, parent_id=None, function_name=None):
    Error_Folder = './API_Error/'
    if os.path.exists(Error_Folder) == True:
        Error_message = f"""
Error Details
Time: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
api_name: {api_name}
function: {function_name}
Response Status Code: {response.status_code}
Response Text: {response.text}
        """
        f = open(f"{Error_Folder}{api_name}-{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}-error.txt", "x")
        f.write(Error_message)
        f.close()
        if api_name == "Webex_api":
            return None
        else:
            send_message(token, room_id, Error_message, parent_id)

    else:
        os.mkdir(Error_Folder)
        handle_api_error(api_name, response, query, token, room_id, parent_id)

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
        handle_api_error("Webex_api", response, None, function_name="get_rooms")
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
    params = {"roomId":{room_id}, "max": 100, "mentionedPeople": "me"} # add  "mentionedPeople": "me" to get spaces recieving to work but cannot send
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        handle_api_error("Webex_api", response, room_id, function_name="get_latest_message")
        return None, None, None

    data = response.json().get("items", [])

    if not data:
        return None, None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", ""), latest.get("personEmail", "")

def send_message(token, room_id, message, parent_id):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "roomId": room_id,
        "text": message,
        "parentId": parent_id
    }
    response = requests.request('POST', url, headers=headers, data = json.dumps(data))
    if response.status_code != 200:
        handle_api_error("Webex_api", response, room_id, function_name="send_message")
        return None

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key, token, room_id, parent_id):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q":{city}, "appid": api_key} 
    response = requests.request('GET', url, params=params)
    print(response)


    if response.status_code != 200:
        handle_api_error("Geocoding_api", response, city, token, room_id, parent_id, function_name="get_city_coordinates")
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key, token, room_id, parent_id):
    location = get_city_coordinates(city, api_key, token, room_id, parent_id)

    if not location:
        return "Location was not found"
    first_lat = location['lat']
    first_lon = location['lon']
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"lat": first_lat, "lon": first_lon, "appid": api_key}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        handle_api_error("Weather_api", response, city, token, room_id, parent_id, function_name="get_weather")
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
def reverse_geocode(lat, lon, api_key, token, room_id, parent_id):
    url = "http://api.openweathermap.org/geo/1.0/reverse"
    params = {
                "lat": lat,
                "lon": lon,
                "limit": 1, 
                "appid": api_key
            }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        handle_api_error("Reverse_Geocoding_api", response, (lat, lon), token, room_id, parent_id, function_name="reverse_geocode")
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key, token, room_id, parent_id):
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)

    if response.status_code != 200:
        handle_api_error("ISS_api", response, None, token, room_id, parent_id, function_name="get_iss_location")
        return None

    data = response.json()

    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']

    location = reverse_geocode(lat, lon, api_key, token, room_id, parent_id)

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
                
    weather_key = api_keys.get("weather_api")
    token = api_keys.get("webex_api")
    rooms = get_rooms(token)

    if not rooms:
        print("No rooms found.")
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text, sender_email = get_latest_message(token, room_id)
        if message_id and message_id != last_message_id:
            if sender_email and sender_email.endswith("@webex.bot"):
                continue

            last_message_id = message_id

            print(f"Received message: {message_text}")
            if message_text.startswith("WT-Lvl5-Assignment1-KY"):
                message_text = message_text[len("WT-Lvl5-Assignment1-KY"):].strip()
            if not message_text.startswith("/"):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit",#
                    parent_id=last_message_id

                )

            elif message_text.lower().startswith("/weather"):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>", parent_id=last_message_id)
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key, token, room_id, parent_id=last_message_id), parent_id=last_message_id)

            elif message_text.lower() == "/iss":
                send_message(token, room_id, get_iss_location(weather_key, token, room_id, parent_id=last_message_id), parent_id=last_message_id)

            elif message_text.lower() == "/quit":
                send_message(token, room_id, "AstroBot shutting down.", parent_id=last_message_id)
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help", parent_id=last_message_id)

        time.sleep(2)



main(api_keys_used, use_hardcoded_key, api_keys_hardcoded)
