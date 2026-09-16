import flask

import requests
from webexpythonsdk import WebexAPI

api = WebexAPI(access_token="NWZmMWJhZDUtMWVjYi00Mzg2LWJlYzMtNWQ1ZGUxZmE1Yjc4YmIwMTY1NTctNWI2_PE93_c18e13ae-5575-4bc0-ae01-e48905f14f17")
BOT_PERSON_ID = api.people.me().id
HTTP_HEADERS = {"User-Agent": "wt-assignment-webex-bot/1.0"}
# Send a message to a specific room
global Glbl_roomId
Glbl_roomId = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMGJlYjkwNjAtYjFhYS0xMWYxLWIzMjEtMGQzYWU2YTViMGRk"


def respond_msg(text, room_id=None):
    room_id = room_id or Glbl_roomId
    api.messages.create(
                roomId=room_id,
                text=text
    )

def weather_api(city):
    city = city.strip()
    if not city:
        return "Usage: /weather <city>"

    geocode_response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"city": city, "format": "json", "limit": 1},
        headers=HTTP_HEADERS,
        timeout=10,
    )
    geocode_data = geocode_response.json()
    print("debug: Geocode response JSON:", geocode_data)
    latitude = geocode_data[0]["lat"]
    longitude = geocode_data[0]["lon"]

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
        },
        timeout=10,
    )
    weather_data = response.json()
    print("debug: Weather response JSON:", weather_data)

    current = weather_data.get("current")

    temperature = current.get("temperature_2m")
    wind_speed = current.get("wind_speed_10m")
    return f"{city.title()}: {temperature}C, wind {wind_speed} km/h"

#flask api for webex
app = flask.Flask(__name__)
@app.route("/webex", methods=["POST"])
def webex_webhook():
    payload = flask.request.get_json(silent=True) or {}
    print("Webhook payload:", payload)

    # Webex webhooks send the message id in payload["data"]["id"].
    message_data = payload.get("data", {})
    if not message_data:
        return "", 200

    # Prevent bot loop: ignore messages sent by the bot itself.
    if message_data.get("personId") == BOT_PERSON_ID:
        return "", 200

    message_id = message_data.get("id")
    if not message_id:
        return "", 200

    try:
        message = api.messages.get(message_id)
    except Exception as exc:
        print("Failed to fetch message details:", exc)
        return "", 200

    text = (message.text or "").strip()
    room_id = message.roomId
    # example msg: @WT... /weather London
    if "/weather" in text:
        city = text[text.find("/weather") + len("/weather"):].strip()
        respond_msg(weather_api(city), room_id=room_id)
    elif "/hello" in text:
        respond_msg("Hello! How can I help you?", room_id=room_id)
    else:
        print("Unknown command:", text)

    return "", 200


if __name__ == "__main__":
    app.run(port=5000)
    print("Flask app running on port 5000")
    print("Webhook endpoint available at /webex")
    print("Global room ID is set to:", Glbl_roomId)
    print("Ready to receive Webex messages.")



