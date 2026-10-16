# Code Review and Explanation, along with development notation and review. 
## Table of Contents


## Function Names and purposes 



# Functions and Their Purposes


# Code Review and Explanation, Along with Development Notation and Review

## Table of Contents
1. [Function Names and Purposes](#1-function-names-and-purposes)
2. [Development Notes and Review](#2-development-notes-and-review)
3. [Program Structure and Execution Flow](#3-program-structure-and-execution-flow)
4. [Testing and Debugging](#4-testing-and-debugging)
5. [Limitations and Future Development](#5-limitations-and-future-development)

## 1. Function Names and Purposes

| Function Name | Description | Invoked By | Invokes |
|---|---|---|---|
| `handle_api_error()` | Handles unsuccessful API responses by logging error details to a file and, where appropriate, reporting them through Webex. This prevents certain application failures by identifying unsuccessful responses before the program attempts to extract data that may not be present, thereby reducing the likelihood of unexpected termination and system downtime. | `get_rooms()`, `get_latest_message()`, `send_message()`, `get_city_coordinates()`, `get_weather()`, `reverse_geocode()`, `get_iss_location()`, `get_word_definition()`, `send_message_file()`, `astronomy_picture_day()`, `get_mars_weather()`, `handle_api_error()` | `send_message()`, `handle_api_error()` |
| `get_api_keys()` | Retrieves the API keys required by the program, initially checking system environment variables and values loaded from the `.env` configuration file. If a required key is unavailable, the function can use a hardcoded key when this option is enabled or request the key interactively from the system administrator running the program. | `main()` | — |
| `get_rooms()` | Interacts with the Webex API to retrieve the messaging rooms to which the bot has access. | `main()` | `handle_api_error()` |
| `print_rooms()` | Displays the names and identifiers of the Webex rooms available to the bot, allowing the system administrator to identify the appropriate messaging space. | `main()` | — |
| `select_room()` | Handles the selection of the active session's Webex messaging room. The selected room ID is subsequently used by the program to determine which messaging space the bot monitors and sends messages to during that session. This limits the program's normal messaging operations to the selected room. | `main()` | — |
| `get_latest_message()` | Interacts with the Webex API to request up to 100 messages from the selected room that mention the bot. The function then extracts the most recent returned message, including its message ID, text and sender's email address, for processing by the main program. | `main()` | `send_message()`, `handle_api_error()` |
| `send_message()` | Interacts with the Webex API to send text messages to the selected messaging room. When provided with a parent message ID, the function sends the message as a reply within the corresponding conversation thread. The main program determines when the function is invoked in response to a recognised bot command. | `main()`, `get_latest_message()`, `handle_api_error()` | `handle_api_error()` |
| `get_city_coordinates()` | Interacts with the OpenWeatherMap Geocoding API to retrieve the geographical coordinates, consisting of latitude and longitude, associated with the city supplied in the user's query. | `get_weather()` | `handle_api_error()` |
| `get_weather()` | Interacts with the OpenWeatherMap API to retrieve current weather information for the latitude and longitude obtained through `get_city_coordinates()`. The retrieved information is formatted into a textual response containing the location, temperature, weather conditions, humidity and wind speed. | `main()` | `get_city_coordinates()`, `handle_api_error()` |
| `reverse_geocode()` | Receives the latitude and longitude associated with the International Space Station's (ISS) reported position. It uses the OpenWeatherMap Reverse Geocoding API to identify a nearby recognised geographical location, where available. If no location is returned, the program uses a fallback description indicating that no nearby city has been identified. | `get_iss_location()` | `handle_api_error()` |
| `get_iss_location()` | Interacts with the Open Notify ISS location API to retrieve the International Space Station's latest available reported latitude and longitude. The coordinates are subsequently passed to `reverse_geocode()` to identify a nearby named geographical location where possible. The resulting information is formatted for presentation to the user. | `main()` | `reverse_geocode()`, `handle_api_error()` |
| `get_word_definition()` | Interacts with the Free Dictionary API to retrieve dictionary information for the word supplied in the user's query. The function selects the first available entry and its first definition, returning the word and corresponding definition as a formatted textual response. | `main()` | `handle_api_error()` |
| `send_message_file()` | Interacts with the Webex messaging API to send a message containing a file attachment URL. When provided with a parent message ID, the message is associated with the corresponding conversation thread. Although the function is designed to support file attachments generally, its current implementation within the program is used to send astronomy-related images. | `main()` | `handle_api_error()` |
| `astronomy_picture_day()` | Interacts with NASA's Astronomy Picture of the Day (APOD) service to retrieve the latest returned astronomy entry, including its title and high-definition media URL where available. The retrieved information is returned to the main program for transmission to the user through `send_message_file()`. | `main()` | `handle_api_error()` |
| `get_mars_weather()` | Interacts with NASA's historical InSight Mars Weather API to request meteorological information collected on Mars. The function is intended to retrieve and return the API response for presentation to the user. However, the feature is currently non-functional because it relies on an outdated API service. | `main()` | `handle_api_error()` |
| `main()` | Acts as the main entry point and control sequence for the program. It initialises the required API keys, retrieves available Webex rooms, allows the administrator to select an active messaging space and continuously monitors incoming messages. It identifies recognised commands, invokes the corresponding functions, sends responses to users, manages polling intervals and handles the program's shutdown command. | Module-level entry point | `get_api_keys()`, `get_rooms()`, `print_rooms()`, `select_room()`, `get_latest_message()`, `send_message()`, `get_weather()`, `get_iss_location()`, `get_mars_weather()`, `get_word_definition()`, `astronomy_picture_day()`, `send_message_file()` |

## 2. Development Notes and Review

The program follows a modular structure in which individual functions are responsible for interacting with specific APIs, processing their responses and returning information to the main control sequence.

The `main()` function coordinates program execution, while supporting functions provide Webex messaging, weather information, ISS tracking, dictionary definitions, astronomy imagery and Mars weather functionality.

API error handling is centralised through `handle_api_error()`. Functions check API response status codes before attempting to process returned data. Where an unsuccessful response is detected, the error-handling function records the relevant details and allows the calling function to return a controlled result rather than proceeding with potentially missing response data.

**Developmental Constraint**  
Due to  design contstrains related to the timeline of the project but also the developmental complexity it was not possible to complete a error handler that was more complex and thorough, important features like handling invalid data, changed endpoints, or advanced reporting like handling expired api keys differently to 301 redirects is not possible. If an API Resource behaves differently in any function to how it does during development it is likely to impact the programes usability, this can be limited to poor performance, degraded usability where messages contain invalid data but could also result in a complete incompatibility and likely throw errors that result in crashes. 

The program currently includes some functionality that remains under development, including the Mars weather service.



## 3. Program Structure and Execution Flow
```flowchart

```

**Design Notes**
The program checks for messages every 10s  
1. No Messages  
1.1 1Repeat
2. Messages  
2.1 Check Messages for tag
....

### 3.1 Program Initialisation
```python

```

**Design Notes**

### 3.2 API Key Retrieval and Configuration
```python

```

**Design Notes**

### 3.3 Webex Room Retrieval and Selection
```python

```

**Design Notes**

### 3.4 Message Monitoring and Polling
```python

```

**Design Notes**

### 3.5 Command Identification and Function Invocation
```python

```

**Design Notes**

### 3.6 Response Processing and Delivery
```python

```

**Design Notes**

### 3.7 Program Termination
```python

```

**Design Notes**


---
