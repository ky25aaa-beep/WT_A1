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
| Provider used (Choose one) | **LocationIQ / Mapbox/ OpenWeatherMap other -provide detail** |
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
| API Provider | '_________' |
| API Base URL | `_______________________________` |
| Endpoint | `_______________________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample JSON response (formatted example) |  
```

```
|

--- 

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

Explain how REST APIs are used in your AstroBot: 

- Describe how HTTP methods (GET, POST) are used  
- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)  
- Describe how JSON responses are received and processed  

Note: Relate your explanation directly to your code for higher grade. 

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