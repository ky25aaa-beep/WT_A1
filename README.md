# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**


---

##  Webex Messaging API (4 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `https://webexapis.com/v1` |
| Authentication Method | Webex access token in the `Authorization` header using the Bearer scheme |
| Endpoint to list rooms | `https://webexapis.com/v1/rooms` |
| Endpoint to get messages | `https://webexapis.com/v1/messages` |
| Endpoint to send message | `https://webexapis.com/v1/messages` |
| Required headers | `Authorization: Bearer <access_token>` and `Accept: application/json`; JSON POST requests also use `Content-Type: application/json` |

#### Sample GET request to retrieve room messages
```python 
url = 'https://webexapis.com/v1/messages'
params = {"roomId": room_id, "max": 100, "mentionedPeople": "me"}
headers = {
  "Authorization": f"Bearer {token}",
  "Accept": "application/json"
}
response = requests.get(url, headers=headers, params=params)
```
---

##  ISS Current Location API (2 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `http://api.open-notify.org/` |
| Endpoint for current ISS location | `http://api.open-notify.org/iss-now.json` |
| Sample response format (example JSON) |  
```json
{"iss_position": {"latitude": "32.5523", "longitude": "155.8306"}, "timestamp": 1790755940, "message": "success"}
```
|

---

##  Geocoding API (4 marks)

| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | OpenWeather |
| API Base URL | `http://api.openweathermap.org/` |
| Endpoint for geocoding | `http://api.openweathermap.org/geo/1.0/direct` |
| Endpoint for reverse geocoding | `http://api.openweathermap.org/geo/1.0/reverse` |
| Authentication method | OpenWeather API key passed as the `appid` query parameter |
| Direct geocoding parameters | `q` (city name) and `appid`; `limit` is optional |
| Reverse geocoding parameters | `lat`, `lon`, and `appid`; `limit` is optional |
| Sample reverse geocoding request | `https://api.openweathermap.org/geo/1.0/reverse?lat=55.86&lon=-4.25&limit=1&appid={API_KEY}` |
| Sample JSON response (formatted example) |  
```json
[
    {
        "name": "Glasgow",
        "local_names": {
            "hi": "ग्लास्गो",
            "mk": "Глазгов",
            "ta": "கிளாஸ்கோ",
            "ko": "글래스고",
            "el": "Γλασκώβη",
            "tl": "Glasgow",
            "ca": "Glasgow",
            "oc": "Glasgow",
            "af": "Glasgow",
            "bs": "Glasgow",
            "th": "กลาสโกว์",
            "uz": "Glazgo",
            "fa": "گلاسگو",
            "ja": "グラスゴー",
            "la": "Glasgua",
            "gl": "Glasgow",
            "ga": "Glaschú",
            "am": "ግላዝጎ",
            "hy": "Գլազգո",
            "lt": "Glazgas",
            "cv": "Глазго",
            "it": "Glasgow",
            "fy": "Glasgow",
            "zh": "格拉斯哥",
            "is": "Glasgow",
            "sr": "Глазгов",
            "pa": "ਗਲਾਸਗੋ",
            "ar": "غلاسكو",
            "bg": "Глазгоу",
            "ps": "ګلاسګو",
            "ms": "Glasgow",
            "tw": "Glasgow",
            "cs": "Glasgow",
            "ce": "Глазго",
            "sd": "گلاسگو",
            "uk": "Глазго",
            "ru": "Глазго",
            "yo": "Glasgow",
            "id": "Glasgow",
            "sk": "Glasgow",
            "sq": "Glasgou",
            "ka": "გლაზგო",
            "he": "גלאזגו",
            "gv": "Glaschu",
            "lv": "Glāzgova",
            "pl": "Glasgow",
            "az": "Qlazqo",
            "mi": "Karahiko",
            "li": "Glasgow",
            "kn": "ಗ್ಲಾಸ್ಗೋ",
            "de": "Glasgow",
            "tt": "Glazgo",
            "ml": "ഗ്ലാസ്ഗോ",
            "pt": "Glasgow",
            "ba": "Глазго",
            "no": "Glasgow",
            "vi": "Glasgow",
            "jv": "Glasgow",
            "nn": "Glasgow",
            "ku": "Glasgow",
            "kv": "Глазго",
            "fi": "Glasgow",
            "es": "Glasgow",
            "bn": "গ্লাসগো",
            "my": "ဂလပ်စဂိုးမြို့",
            "ky": "Глазго",
            "mr": "ग्लासगो",
            "et": "Glasgow",
            "sh": "Glasgow",
            "ug": "Glasgow",
            "gd": "Glaschu",
            "te": "గ్లాస్గో",
            "nl": "Glasgow",
            "mn": "Глазго",
            "eo": "Glasgovo",
            "yi": "גלאזגא",
            "tr": "Glasgow",
            "cy": "Glasgow",
            "fo": "Glasgow",
            "ro": "Glasgow",
            "sa": "ग्लास्गो",
            "co": "Glasgow",
            "en": "Glasgow",
            "sl": "Glasgow",
            "tg": "Глосгу",
            "fr": "Glasgow",
            "kw": "Glaschu",
            "hr": "Glasgow",
            "da": "Glasgow",
            "sv": "Glasgow",
            "ur": "گلاسگو",
            "os": "Глазго",
            "sw": "Glasgow",
            "hu": "Glasgow",
            "ha": "Glasgow",
            "br": "Glasc'ho",
            "qu": "Glasgow",
            "be": "Глазга",
            "eu": "Glasgow",
            "kk": "Глазго"
        },
        "lat": 55.861155,
        "lon": -4.2501687,
        "country": "GB",
        "state": "Scotland"
    }
]
```
|

---


##  Weather API (3 marks)

| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | Openweathermap |
| API Base URL | `https://api.openweathermap.org/` |
| Endpoint for current weather | `https://api.openweathermap.org/data/2.5/weather` |
| Authentication method | OpenWeather API key passed as the `appid` query parameter |
| Required query parameters | `lat`, `lon`, and `appid`; the bot also sends `units=metric` to request Celsius |
| Sample JSON response (formatted example) |  
```json
{
    "coord": {
        "lon": -0.1278,
        "lat": 51.5074
    },
    "weather": [
        {
            "id": 501,
            "main": "Rain",
            "description": "moderate rain",
            "icon": "10d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 14.69,
        "feels_like": 14.62,
        "temp_min": 13.34,
        "temp_max": 15.31,
        "pressure": 1012,
        "humidity": 92,
        "sea_level": 1012,
        "grnd_level": 1009
    },
    "visibility": 1735,
    "wind": {
        "speed": 1.54,
        "deg": 340
    },
    "rain": {
        "1h": 2.05
    },
    "clouds": {
        "all": 100
    },
    "dt": 1791361483,
    "sys": {
        "type": 2,
        "id": 2075535,
        "country": "GB",
        "sunrise": 1791353431,
        "sunset": 1791393960
    },
    "timezone": 3600,
    "id": 2643743,
    "name": "London",
    "cod": 200
}

```
|
s
---

##  Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details |
|---------|---------|
| Library used | `datetime` module |
| Function used to convert epoch | `datetime.fromtimestamp()` |
| Sample code to convert timestamp |  
```python
from datetime import datetime, timezone

def epoch_to_human_time(timestamp):
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )

print(epoch_to_human_time(1790755940))
```
| Output (human-readable time) | `2026-09-30 08:12:20 UTC` |

---

##  Free Dictionary API (used by `/define`)

| Criteria | Details |
|---------|---------|
| API Provider | 'https://freedictionaryapi.com' |
| API Base URL | `https://freedictionaryapi.com/api/v1` |
| Endpoint | `https://freedictionaryapi.com/api/v1/entries/en/{word}` |
| Authentication method | `none` |
| Required query parameters | `none` |
| Sample JSON response (formatted example) |  
```json
{
  "word": "hello",
  "definitions": [
    {
      "partOfSpeech": "interjection",
      "senses": [
        "A greeting (salutation) said when meeting someone or acknowledging someone s arrival or presence.",
        "A greeting used when answering the telephone.",
        "A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.",
        "(colloquial) Used sarcastically to imply that the person addressed has done something the speaker considers to be foolish, or missed something that should have been obvious.",
        "(chiefly UK) An expression of puzzlement or discovery."
      ]
    },
    {
      "partOfSpeech": "noun",
      "senses": [
        "\"Hello!\" or an equivalent greeting."
      ]
    },
    {
      "partOfSpeech": "verb",
      "senses": [
        "(transitive) To greet with \"hello\"."
      ]
    }
  ]
}

```
|

--- 
**Json has been shortned as response contains pronounciation variations for regions and english is spoken all over the place and therefore there are hundreds of entries**

##  Extended Feature API: NASA APOD (3 marks)

| Criteria | Details |
|---------|---------|
| API Provider | NASA APOD data served by NASA Science |
| Endpoint used in the code | `https://science.nasa.gov/wp-json/wp/v2/apod-basic` |
| Authentication method | None used by this endpoint in the current implementation |
| Query parameters | `page=1` and `per_page=1` |
| Response data used | The response is a JSON list. The bot reads the first item's `title` and `hdurl`, or `url` if `hdurl` is not present. |
| Bot command | `/astronomy` |

The `/astronomy` command sends the returned title and image URL to Webex. The Free Dictionary API is a separate feature used by `/define`, rather than the astronomy extension.

##  Evaluation – Web Architecture, MVC Design & Security 

In this section, evaluate how web technologies, architecture, and design patterns have been applied in your **AstroBot**. Your responses must relate directly to your implementation and include reflection on your design decisions.

---

###  Web Architecture – Client–Server Model (3 marks)
Astrobot is built in line with the client-server architecture model. The client is the webex application itself that the astronomy club members use to interact with the bot. The Python Astrobot also acts as a http client as it sends request to its API's. While also being the server in the webex-python relationship. 

The main server invvolved is the webex server that the python bot communicates with to handle sending and recieving messages. Other Servers include Nasa's APOD and OpenNotify, and Openweather for Geocoding and Weather Information. 

Astrobot uses polling to retrieve messages  regularly from the webex server, rather than hosting a web server to recieve them via web request. Instead it sends GET requests to the webex Messaging API and evaluates whether the message contains a command. 

**Example data flow:**
1. The user sends /weather London through the Webex Apllication {client}
2. Webex Receives and stores the message on its servers {server}
3. Astrobot sends a GET request to the Webex Messaging API to retrieve messages {client}
4. Webex Responds with the messaging information {server}
5. Astrobot Recieves the messages and evaluates the contents {client}
6. Astrobot identifies the weather command and extracts the location London {server}
7. Astrobot Sends a request to the geocoding api to convert london to latitude and longitude {client}
8. The geocoding api converts the values and responds with the information {server}
9. Astrobot sends those coordinates to the weather API to retrieve the current weather conditions {client}
10. The Weather API Openweather processes the request and responds {server}
11. Astrobot recieves the request and formats a response {server}
12. Astrobot sends a post request to the messaging api containing the response {client}
13. The Webex Server responds with a 200 and stores the reply {server}
14. The user is shown the response on the Webex Application {client}

![NASA API key correction](<Development Issues and Notes/Diagram.png>)

####  Security Considerations: (3 marks )
Most of the external services used by AstroBot support HTTPS, which encrypts the communication between the application and the API server using TLS.

This is particularly important when transmitting authentication credentials or accessing user messages through Webex.HTTPS encrypts traffic with an ssl certificate. 

One current issue is the Open Notify ISS endpoint, is independently run and while it serves iss data it is not a NASA projcet and is only served over HTTP not HTTPS.

Overall, AstroBot addresses some of the main security risks through environment variables and API rate-limit handling. Further improvements could include stricter input validation, request timeouts and more consistent handling of unexpected API responses.
---

###  RESTful API Usage in Your Application (3 marks )

Astrobot uses RESTful APIs, Instead of treating the server like a list of random functions to execute, a RESTful API treats everything on the server as a resource (such as a user, a product, or an image). Each resource is given a unique web address called a URI (Uniform Resource Identifier) or endpoint.

#### GET Requests
The bot uses GET requests to retrieve Webex messages, dictionary entries, NASA APOD data, OpenWeather weather and geocoding data, and the ISS position from Open Notify. It uses POST requests to send messages to Webex.

#### POST Requests
The API pushes (posts) messages to the webex api containing the new message content 

#### How Requests are formatted

Each API has its own endpoints and required parameters. For example, the Webex Messages endpoint is `https://webexapis.com/v1/messages`. Webex identifies the account with an access token in the `Authorization` header using the Bearer scheme. The message-list request includes a `roomId` and can include filters such as `max` and `mentionedPeople`. OpenWeather requests use the `appid` query parameter for the API key, while the ISS location endpoint used here does not require parameters or authentication. Successful requests return JSON data that the bot parses and formats for Webex.

The Free Dictionary endpoint places the requested word in its URL path, so `/define hello` requests the `hello` entry. It does not require authentication. This differs from OpenWeather's query-parameter API key and Webex's Bearer access token.

#### How API's/Endpoints Respond

An HTTP response includes a three-digit status code. The code indicates whether the request succeeded or whether an error occurred; status codes are integers, not decimal values. Common ranges are:

1xx - Informational (100 Continue, 101 Switching Protocols )
2xx - Successful (200 OK, 201 Created, 204 No Content (DELETE WORKED))
3xx - Redirection (301 Permanent Move, 302 Temporary Redirect/Found)
4xx - Client Side Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too many Requests)
5xx - Server Side Error (500 Internal Server Error, 502 Bad Gateway, 503 Server Unavailable)

#### How Requests are handled in code 

**HTTP REsponse Code: 429**
```python
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 429:
        global retry_after
        retry_after = int(response.headers.get("Retry-After", 60))  # Default to 60 seconds if not provided
        print(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
        send_message(token, room_id, "Webex request limits have been reached. The bot is currently operating at a slower pace to process everything smoothly. Please allow a little extra time for responses.", parent_id=None)
        time.sleep(retry_after)  # Wait for the specified time before retrying
```

This code makes a request to the url "url" with specified headers and parameters in the request. It makes a get request that returns a response we are calling response. This response is then checked for a status code, if that code is 429 the code then sets a variable called retry_after, the value of that variable is the valuye stored in the responses header that is called Retry-After and according to webex's api should be set on a 429 response, if it is not it sets it as 60 seconds. 

```python
    if response.status_code != 200:
```

Checking only for `200` can incorrectly treat another successful status as a failure. For example, `201` means the request succeeded and created a resource, and `204` means it succeeded with no response body. The accepted success codes should match the endpoint's documented responses; the web server software does not change a status code into a decimal.
```python 
if response.status_code not in [200, 201, 204]:
```
This code is instead prefered and checks whether the request wasn't succesful. While currently none of the API's use these subcodes, it should be added now to future proof the code for future development. 

---

###  MVC Design Pattern in AstroBot (3 Marks)



| Component   | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model**  | Handles data retrieval, storage, and processing. In my bot, this includes: the API error handler; weather API; nasa APIs ; and environment variable loading. **Example:** When the user sends a /weather <city> message the API retrieving the lat and long of that location, parses JSON, and processing it for the openweather function|
| **View**   | Responsible for presenting information to the user. In my bot, this includes: the formatting functions that build easy to read webex responses. **Example:** After the model returns weather data the format_weather_report makes the response is visually acceptable. 
| **Controller** | Handles system functions, In my bot this can be the API key handling, selecting functions/commands and polling functions. **Example:**  After the user sends a message containing /weather <city> the program selects the function get_weather_coordinates|

---

### 📝 Reflection and Evaluation ( 8 marks )

The astrobot functionally is good at meeting the Astronomy Club's Needs, for now it can affectively respond to commands, communicate in teams and in direct message spaces, the most beneficial design desision was to use the mentionedPeople parameter in the get_latest_messages functions webex api call, this meant the bot could work ingroups as well as direct messages. The most challenging aspect of integrating APIs especially the nasa API's was finding an api endpoint that had been retrieved or who's documentation had yet to be updated. The biggest security risk were the tokens and api keys, the solution to them being leaked being adding them as environment variables in a .env file. The solution could be improved in the future by better error handling and a more robust webex api, as some 429 errors are recieved after approximately 1 hour of activity, the imporvement would be polling for messages more frequently during active periods and less frequently in inactive periods. 

```pseudocode

IF latest_message == "":
    unsuccessful_polls += 1
    IF unsuccessful_polls > 10
        poll_delay += 10 
    ELSE IF unsuccessful_polls >5:
        poll_delay += 5
    ELSE: 
        poll_delay +=1

ELSE:
    unsuccessful_polls = 0
    poll_delay = 0
```

---

### Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

###  Total: /40
