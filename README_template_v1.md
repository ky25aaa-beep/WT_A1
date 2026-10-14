# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also furhter investigate the application of Web Architecture and MVC design pattern in development of the Bot

---

##  Webex Messaging API (4 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `https://webexapis.com/v1` |
| Authentication Method | `api key` |
| Endpoint to list rooms | `https://webexapis.com/v1/rooms` |
| Endpoint to get messages | `https://webexapis.com/v1/messages` |
| Endpoint to send message | `https://webexapis.com/v1/messages` |
| Required headers | `bearer token and methods, if theres a response containing data that datas format` |

#### Sample full GET or POST request  
```python 
url = `https://webexapis.com/v1/messages`
params = {"roomId":{room_id}, "max": 100}
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
| Endpoint for current ISS location | `http://api.open-notify.org/iss-now.json_` |
| Sample response format (example JSON) |  
```json
{"iss_position": {"latitude": "32.5523", "longitude": "155.8306"}, "timestamp": 1790755940, "message": "success"}
```
|

---

##  Geocoding API (4 marks)

| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | OpernWeatherMap.org |
| API Base URL | `http://api.openweathermap.org/` |
| Endpoint for geocoding | `http://api.openweathermap.org/geo/1.0/direct` |
| Endpoint for reverse geocoding | `http://api.openweathermap.org/geo/1.0/reverse` |
| Authentication method | `parameter appid/apikey` |
| Required query parameters | `q and appid` |
| Sample request with latitude/longitude | `
                "lat": lat,
                "lon": lon,
                "limit": 1, 
                "appid": api_key` |
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
| API Provider (Choose one) | **OpenWeather, OpenWeatherMap (or other – provide details)** |
| API Base URL | `http://api.openweathermap.org/` |
| Endpoint for current weather | `http://api.openweathermap.org/data/2.5/weather` |
| Authentication method | `parameter api key` |
| Required query parameters | `"lat": first_lat, "lon": first_lon, "appid": api_key` |
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
        "temp": 287.84,
        "feels_like": 287.77,
        "temp_min": 286.49,
        "temp_max": 288.31,
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
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |  
```  
```
|
| Output (human-readable time) | `_______________________________` |

---

##  Extended Feature API ( 3 marks)

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

##  Evaluation – Web Architecture, MVC Design & Security 

In this section, evaluate how web technologies, architecture, and design patterns have been applied in your **AstroBot**. Your responses must relate directly to your implementation and include reflection on your design decisions.

---

###  Web Architecture – Client–Server Model (3 marks)

Explain how the client–server model applies to your AstroBot:

- Identify the **client** 
- Identify the **server(s)** 
- Describe how data flows between:
  - User, AstroBot and APIs

Include a **simple block diagram** to illustrate this interaction.

####  Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate limiting, and Input validation (e.g., handling user commands safely), include examples from code where necessary to illustrate.

---

###  RESTful API Usage in Your Application (3 marks )

Astrobot uses RESTful APIs, Instead of treating the server like a list of random functions to execute, a RESTful API treats everything on the server as a resource (such as a user, a product, or an image). Each resource is given a unique web address called a URI (Uniform Resource Identifier) or endpoint.

#### GET Requests
The API requests the latest messages from the webex api; it also requests the definition of words from the dictionary api; the astronomical photo of the data from the nasa api; the weather and geolocation data from the openweather api, and finally the position of the iss from the nasa api. 

#### POST Requests
The API pushes (posts) messages to the webex api containing the new message content 

#### How Requests are formatted

Every api has their own required formatting but the overall idea is fairly similar, there is a specific endpoint for that function we call this a resource and for an example https://webexapis.com/v1/messages. This is the specific endpoint for the messages resource the api itself sits in https://webexapis.com/v1, the webex api requires authentication and like most apis this is as an apikey provided in the http message, for some more modern systems this is as a token in the authorisation header, a portion of a http request that is specified for this exact purpose. If the authentication is successful the request is then handled by the api, it usually does some processing then returns a result for most apis this is json but it could be any format. Most Api's take the information they need to process a request in the parameters field for the messages api (this returns the messages in a particular room in webex) the api needs room ID, but it can filter with specifics like max and mentionedpeople. 

While most restful api's work like this some apis handle data requests differently, apis like the freedictionary api don't require authorisation and dont use the requests field instead they are simplified as the api only requires the singular paramter word to define they take it as a specific resource under the endpoint /v1/entries/en. This still uses the same get request just has a different way of providing request data. There is a limitation to this method that only 1 data point is parsable and the avoidance of an api token means the api has no way to validate requests. However as the endpoint handles no private data just being a dictionary it doesn't require this from a security standpoint. 

#### How API's/Endpoints Respond

Once a HTTP Request is made whether that is GET, POST, POST, DELETE. The Server will response all responses have a code these codes are three digits long usually (can contain a decimal i.e xxx.xx) they have the following meanings:

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

This is a similar bit of code but instead of matching if the code is 429 it checks if it isn't 200, this code isn't perfect if the api uses asp.net and returns 200.0 unlike apache it will fail, if the response contains 201/204 instead of 200 it will falsely capture a successful request as unsuccessful. 
```python 
if response.status_code not in [200, 201, 204]:
```
This code is instead prefered and checks whether the request wasn't succesful. 
#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses, Avoiding excessive API calls

---

###  MVC Design Pattern in AstroBot (3 Marks)

Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation

| Component   | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model**  |  |
| **View**   |  |
| **Controller** |  |

---

### 📝 Reflection and Evaluation ( 8 marks )

Reflect on your AstroBot (400 words):

- How effective is your bot in meeting the Astronomy Club’s needs?  
- What design decisions worked well?  
- What challenges did you face when integrating APIs?  
- What security risks did you identify and how were they handled?  
- How could your solution be improved in the future?  

---

 **Tip:** Link your answers directly to your code and examples for higher marks.
### Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

###  Total: /40