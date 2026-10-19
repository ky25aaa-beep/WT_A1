# Code Review and Development Notation

## Table of Contents
1. [Function Names and Purposes](#1-function-names-and-purposes)
2. [Development Notes and Review](#2-development-notes-and-review)
3. [Program Structure and Execution Flow](#3-program-structure-and-execution-flow)
4. [Testing and Development](#4-testing-and-development)
5. [Limitations and Future Development](#5-limitations-and-future-development)

## 1. Function Names and Purposes

| Function Name | Description | Invoked By | Invokes |
|---|---|---|---|
| `handle_api_error()` | Handles unsuccessful API responses by logging error information to a file.The program will atempt to send the error information over webex, however in the event the error is relating to webex it will not. This prevents certain application failures by identifying unsuccessful responses before the program attempts to extract data that may not be present, thereby reducing the likelihood of unexpected termination and system downtime. | `get_rooms()`, `get_latest_message()`, `send_message()`, `get_city_coordinates()`, `get_weather()`, `reverse_geocode()`, `get_iss_location()`, `get_word_definition()`, `send_message_file()`, `astronomy_picture_day()`, `get_mars_weather()`, `handle_api_error()` | `send_message()`, `handle_api_error()` |
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

Functions are designed to be self-contained, and responsible for a single function, and be reusable across different parts of the program. This design allows for easier maintenance, testing and future expansion.For example, the `get_city_coordinates()` function is used by weather to get a city's coordinates, however it could also be used by other functions that require geographical coordinates for a given city.

The `main()` function coordinates program execution, while supporting functions provide Webex messaging, weather information, ISS tracking, dictionary definitions, astronomy imagery and Mars weather functionality.

API error handling is centralised through `handle_api_error()`. Functions check API response status codes before attempting to process returned data. Where an unsuccessful response is detected, the error-handling function records the relevant details and allows the calling function to return a controlled result rather than proceeding with potentially missing response data.

**Developmental Constraint**  
Due to  design contstrains related to the timeline of the project but also the developmental complexity it was not possible to complete a error handler that was more complex and thorough, important features like handling invalid data, changed endpoints, or advanced reporting like handling expired api keys differently to 301 redirects is not possible. If an API Resource behaves differently in any function to how it does during development it is likely to impact the programes usability, this can be limited to poor performance, degraded usability where messages contain invalid data but could also result in a complete incompatibility and likely throw errors that result in crashes. 

The program currently includes some functionality that remains under development, including the Mars weather service.



## 3. Program Structure and Execution Flow

The AstroBot program uses a modular, sequential execution structure, with `main()` acting as the primary control function. The program is designed to continuously monitor a selected Cisco Webex messaging room, identify incoming commands and invoke the appropriate functions to retrieve information from external APIs.

The program follows a polling-based approach rather than using Webex webhooks or an event-driven messaging system. This means that it periodically requests messages from the Webex API to determine whether a new command has been received.

The execution process can be divided into seven stages: program initialisation, API key retrieval, Webex room selection, message monitoring, command processing, response delivery and program termination.

### Program Execution Flowchart

```
```

**Design Notes**

The program follows a continuous monitoring process after initialisation has completed. This is achieved through repated invocation of `get_latest_message()` within an indefinite loop.

Under normal operation, the program waits approximately ten seconds between message polling operations, although the exact timing can vary depending on if the Webex API returns a `retry-after` value in its response headers.

1. **No new message detected:** The program waits before checking the Webex API again.
2. **New message detected:** The program checks whether the message was sent by a bot account.
3. **Bot-generated message:** The message is ignored.x
4. **User-generated message:** The program processes its text and checks whether it contains a command.
5. **Recognised command:** The appropriate function is invoked to retrieve or process the requested information.
6. **Unrecognised command:** The program sends an error message explaining that the command is not recognised.
7. **Shutdown command:** The program sends a shutdown notification and exits the monitoring loop and subsequent operations.

---

### 3.1 Program Initialisation

The program starts by importing the libraries required for API communication (requests), JSON handling (json), date and time management (datetime), execution delays (time), environment variable access (os, dotenv).

**Python Code**

```python
import requests
import json
from datetime import datetime
import time
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

global use_hardcoded_key

use_hardcoded_key = False

api_keys_used = (
    "weather_api",
    "webex_api",
    "NASA_api",
    "Geocoding_api"
)

api_keys_hardcoded = {
    "weather_api": "provide_key",
    "webex_api": "provide_key",
    "NASA_api": "provide_key",
    "Geocoding_api": "provide_key",
}
```

The program subsequently invokes the main control function:

```python
main(
    api_keys_used,
    use_hardcoded_key,
    api_keys_hardcoded
)
```

**Design Notes**

The `requests` library provides the HTTP functionality required to communicate with the external APIs used throughout the program.

The `json` library is used to serialise information when transmitting messages to the Webex API.

The `datetime` library is used when generating timestamps for API error logs, allowing errors to be associated with the date and time at which they occurred.

The `time` library provides the delays required by the message polling mechanism and the existing rate-limit handling logic.

The `os` library allows the program to access system environment variables and perform file system operations, including creating the directory used for error logging.

The `python-dotenv` library allows configuration values from a `.env` file to be loaded into the program's environment.

The `use_hardcoded_key` variable determines whether the program should use hardcoded credentials when environment variables are unavailable.

It is initially configured as `False`, meaning that interactive administrator input is used as the fallback rather than the hardcoded values. During Development this can be set to True to allow the program to run without requiring interactive input, environment variables or a `.env` file. Instead using values supplied in the `api_keys_hardcoded` dictionary.

**Development Consideration**

The program executes `main()` directly at module level, meaning that importing the Python file into another program would also start the bot.

A future implementation could use the conventional `if __name__ == "__main__":` entry-point structure to prevent automatic execution when the module is imported.

---

### 3.2 API Key Retrieval and Configuration

Once `main()` has been invoked, the program retrieves the API credentials required to communicate with external services.

This process is handled through the `get_api_keys()` function.

**Python Code**

```python
def get_api_keys(
    api_keys_used,
    use_hardcoded_key,
    api_keys_hardcoded
):
    api_keys = {}

    for key_name in api_keys_used:
        env_var_name = f"{key_name}_key"

        api_key = os.getenv(env_var_name)

        if not api_key:
            print(
                f"Error: {env_var_name} not found "
                "in environment variables. "
                "using hardcoded key instead."
            )

            if use_hardcoded_key:
                api_key = api_keys_hardcoded.get(key_name)

            else:
                api_key = str(
                    input(
                        f"Provide API Key for api: "
                        f"{key_name}: "
                    )
                )

        api_keys[key_name] = api_key

    return api_keys
```

The function is invoked within `main()`:

```python
api_keys = get_api_keys(
    api_keys_used,
    use_hardcoded_key,
    api_keys_hardcoded
)

weather_key = api_keys.get("weather_api")
token = api_keys.get("webex_api")
nasa_key = api_keys.get("NASA_api")
```

**Design Notes**

The program uses a three-part credential retrieval approach.

1. **Environment Variables:** The function initially attempts to retrieve each required API key from the environment. This includes values loaded from the `.env` configuration file.

2. **Hardcoded Credentials:** If the environment variable is unavailable and `use_hardcoded_key` is enabled, the function attempts to retrieve the corresponding credential from the `api_keys_hardcoded` dictionary.

3. **Administrator Input:** If the environment variable is unavailable and hardcoded credentials are disabled, the program requests the missing key interactively from the administrator.

The retrieved credentials are stored in a dictionary, allowing other functions to access them using their associated key names.

This design allows configuration information to be separated from the functions responsible for API communication.

It also provides flexibility during development, as credentials can be supplied through different mechanisms without changing individual API functions.

**Development Consideration**

The current console message states that a hardcoded key will be used whenever an environment variable is missing, even when the hardcoded-key option is disabled.

This message does not accurately describe the interactive fallback behaviour.

Also, the function does not validate whether a supplied API key is active, expired or authorised to access the intended service. Credential validity is therefore only established indirectly when subsequent API requests are made.

---

### 3.3 Webex Room Retrieval and Selection

After API credentials have been retrieved, the program connects to the Webex API to identify the messaging rooms accessible to the bot.

This stage involves three functions:

- `get_rooms()`
- `print_rooms()`
- `select_room()`

**Python Code**

```python
rooms = get_rooms(token)

if not rooms:
    print("No rooms found.")
    return

print_rooms(rooms)

room_id = select_room(rooms)
```

The room retrieval process is performed using the Webex Rooms endpoint:

```python
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

    if response.status_code not in [200, 201, 204]:
        handle_api_error(
            "Webex_api",
            response,
            None,
            function_name="get_rooms"
        )
        return []

    return response.json().get("items", [])
```

The administrator selects a room through the following function:

```python
def select_room(rooms):
    while True:
        name = input("Enter the room name: ")

        for room in rooms:
            if name.lower() in room["title"].lower():
                print(
                    f"Selected room: {room['title']}"
                )
                return room["id"]

        print("Room not found. Please try again.")
```

**Design Notes**

The room retrieval function sends an authenticated request to the Webex API and retrieves a collection of messaging rooms.

The `print_rooms()` function displays the retrieved room names and identifiers to the administrator.

The administrator then selects a room by entering its name.

The selection process is case-insensitive and supports partial name matching.

Once a matching room is found, its identifier is returned to `main()` and stored in `room_id`.

This identifier is subsequently passed to the functions responsible for retrieving and sending messages.

The design provides administrator control over the active messaging space without requiring the administrator to manually enter a Webex room identifier.

**Development Consideration**

If multiple rooms contain the same search term, the program selects the first matching room.

The program also does not provide a command to change the selected room while it is running. A different room can only be selected by restarting the program and repeating the initialisation process.

If the Webex API returns no rooms or an unsuccessful response, `main()` terminates rather than attempting to reconnect automatically.

---

### 3.4 Message Monitoring and Polling

Following room selection, the program begins monitoring the selected Webex messaging space for incoming commands.

The program implements polling by repeatedly invoking `get_latest_message()` within an indefinite loop.

**Python Code**

```python
last_message_id, _, _ = get_latest_message(
    token,
    room_id
)

while True:
    message_id, message_text, sender_email = (
        get_latest_message(token, room_id)
    )

    if message_id and message_id != last_message_id:

        if sender_email and sender_email.endswith(
            "@webex.bot"
        ):
            continue

        last_message_id = message_id

        print(f"Received message: {message_text}")
```

The program retrieves messages through the Webex Messages endpoint:

```python
def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"

    params = {
        "roomId": {room_id},
        "max": 100,
        "mentionedPeople": "me"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )
```

The polling delay is applied at the end of the monitoring loop:

```python
if 'retry_after' in globals():
    time.sleep(retry_after)
else:
    time.sleep(10)
```

**Design Notes**

When monitoring begins, the program retrieves the latest message and stores its identifier in `last_message_id`.

This establishes an initial reference point, preventing the most recently retrieved message from automatically being treated as a new command when the monitoring loop begins.

On subsequent iterations, the program retrieves the latest available message and compares its identifier against the stored value.

If the identifiers are different, the program treats the message as new.

Messages originating from accounts with email addresses ending in `@webex.bot` are ignored to reduce the likelihood of the bot responding to automated messages.

Under normal circumstances, the program waits ten seconds before polling the Webex API again.

**Development Consideration**

Although the API request specifies a maximum of 100 messages, the implementation only processes the first returned message.

This means that messages arriving between polling intervals may be missed if several new messages are received before the next request.

The current implementation also contains an issue with the `roomId` query parameter, which is constructed as a Python set rather than a string.

Certain branches use `continue` before reaching the polling delay. This may cause the program to perform additional API requests without waiting for the intended ten-second interval.

The system therefore provides basic message monitoring but does not implement a complete message queue or guaranteed processing of every received command.

---

### 3.5 Command Identification and Function Invocation

Once a new message has been identified, the program examines its text to determine whether it contains a recognised command.

Commands are identified using a forward slash (`/`) and are processed through conditional statements within `main()`.

**Python Code**

```python
if message_text.startswith("Bot"):
    message_text = message_text[len("Bot"):].strip()

if not message_text.startswith("/"):
    continue
```

Following this initial check, the program compares the message against the supported commands.

```python
if message_text.lower() == "/help":
    send_message(
        token,
        room_id,
        "/weather <city>\n/iss\n/help\n/quit\n/astronomy",
        parent_id=last_message_id
    )

elif message_text.lower().startswith("/weather"):
    parts = message_text.split(maxsplit=1)

    if len(parts) < 2:
        send_message(
            token,
            room_id,
            "Usage: /weather <city>",
            parent_id=last_message_id
        )

    else:
        city = parts[1]
        send_message(
            token,
            room_id,
            get_weather(
                city,
                weather_key,
                token,
                room_id,
                parent_id=last_message_id
            ),
            parent_id=last_message_id
        )
```

Other recognised commands invoke their corresponding functions:

| Command | Function Invoked |
|---|---|
| `/help` | `send_message()` |
| `/weather <city>` | `get_weather()` |
| `/iss` | `get_iss_location()` |
| `/mars_weather` | `get_mars_weather()` |
| `/define <word>` | `get_word_definition()` |
| `/astronomy` | `astronomy_picture_day()` |
| `/quit` | `send_message()`, followed by termination of the monitoring loop. |

**Design Notes**

The program first checks for the text prefix `Bot` and removes it when present. this can be changed to be a different bot name by changing the string in the `startswith()` check and the length of the string used to slice the message text.

It then verifies that the remaining message begins with `/`.

Messages that do not begin with a forward slash are ignored.

The program uses a sequence of `if` and `elif` statements to compare the command against its supported functionality.

For commands requiring additional information, such as `/weather` and `/define`, the program separates the command from its argument using `split(maxsplit=1)`.

The extracted argument is then passed to the relevant function.

For example, a `/weather London` command results in `London` being passed to `get_weather()`, which subsequently invokes `get_city_coordinates()` before retrieving the weather information.

This structure allows individual features to remain separated into their own functions while being coordinated through the main control sequence.

Preferably, the program should be designed to utilise a variable or configuration file to store the bot's name, allowing it to be changed without modifying the source code.

**Development Consideration**

Command recognition is relatively simple and does not use a dedicated command parser.

The `/weather` and `/define` branches use `startswith()` rather than exact command matching, meaning that other messages beginning with those strings may also be interpreted as commands.

Although the program converts commands to lowercase for comparisons, removal of the `Bot` prefix is case-sensitive.

These limitations could be addressed through more robust command parsing and input validation. For example:

```python
def cmd_args(message_text, command_prefix="/", bot_prefix="Bot" ):
    if message_text.lower().startswith(bot_prefix.lower()):
        message_text = message_text[len(bot_prefix):].strip()

    if not message_text.startswith(command_prefix):
        return None, None

    parts = message_text.split(maxsplit=1)
    command = parts[0].lower()
    argument = parts[1] if len(parts) > 1 else None

    return command, argument
def cmd_selector(command, argument):
    #use regex to validate command and argument
    if command == "/help":
        send_message(
            token,
            room_id,
            "/weather <city>\n/iss\n/help\n/quit\n/astronomy",
            parent_id=last_message_id
        )
    elif command == "/weather" and argument:
        send_message(
            token,
            room_id,
            get_weather(
                argument,
                weather_key,
                token,
                room_id,
                parent_id=last_message_id
            ),
            parent_id=last_message_id
        )
    elif command == "/define" and argument:
        send_message(
            token,
            room_id,
            get_word_definition(
                argument,
                token,
                room_id,
                parent_id=last_message_id
            ),
            parent_id=last_message_id
        )
        elif command == "/iss":
            send_message(
                token,
                room_id,
                get_iss_location(
                    token,
                    room_id,
                    parent_id=last_message_id
                ),
                parent_id=last_message_id
            )
        elif command == "/mars_weather":
            send_message(
                token,
                room_id,
                get_mars_weather(
                    nasa_key,
                    token,
                    room_id,
                    parent_id=last_message_id
                ),
                parent_id=last_message_id
            )
        elif command == "/astronomy":
            apod_data = astronomy_picture_day(
                token,
                room_id,
                parent_id=last_message_id
            )

            if apod_data:
                send_message_file(
                    token,
                    room_id,
                    parent_id=last_message_id,
                    **apod_data
                )
        elif command == "/quit":
            send_message(
                token,
                room_id,
                "AstroBot shutting down.",
                parent_id=last_message_id
            )
            break
        else:
            send_message(
                token,
                room_id,
                "Unrecognised command. Type /help for a list of available commands.",
                parent_id=last_message_id
            )
```

---

### 3.6 Response Processing and Delivery

After a recognised command has been executed, the program sends the resulting information back to the selected Webex messaging space.

The program supports two primary response mechanisms:

1. Text-based responses through `send_message()`.
2. File or image responses through `send_message_file()`.

**Python Code**

```python
def send_message(
    token,
    room_id,
    message,
    parent_id
):
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

    response = requests.request(
        'POST',
        url,
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code not in [200, 201, 204]:
        handle_api_error(
            "Webex_api",
            response,
            room_id,
            function_name="send_message"
        )
        return None
```

For astronomy images, the program first retrieves the image information:

```python
elif message_text.lower() == "/astronomy":
    apod_data = astronomy_picture_day(
        token,
        room_id,
        parent_id=last_message_id
    )

    if apod_data:
        send_message_file(
            token,
            room_id,
            parent_id=last_message_id,
            **apod_data
        )
```

**Design Notes**

The functions responsible for retrieving information from external APIs generally return their results to `main()`.

The main function subsequently invokes `send_message()` to transmit the returned information to Webex.

Responses include a `parentId` value that identifies the original message being replied to.

This allows Webex to associate the bot's response with the message that invoked the command.

The program uses JSON to construct outgoing message data and sends the request using the HTTP POST method.

For astronomy imagery, the `astronomy_picture_day()` function returns a dictionary containing the image title and media URL.

The dictionary is unpacked using Python's `**` operator when passed to `send_message_file()`.

This allows the image-related response data to be passed directly to the file messaging function.

in python ** asterisk is used to unpack a dictionary into keyword arguments when calling a function. This means that each key-value pair in the dictionary is treated as a separate argument, allowing for more flexible and dynamic function calls.

**Development Consideration**

The existing implementation does not guarantee that every response is successfully delivered.

Although unsuccessful HTTP status codes are reported through `handle_api_error()`, the program does not automatically retry failed message submissions.

The file attachment mechanism also depends on the Webex API accepting the supplied media URL in the specified request structure.

Additional validation and response confirmation could improve the reliability of message delivery.



---

### 3.7 Program Termination

The program is designed to continue monitoring messages until a recognised shutdown command is received or execution is interrupted.

The `/quit` command provides a method of terminating the program through Webex.

**Python Code**

```python
elif message_text.lower() == "/quit":
    send_message(
        token,
        room_id,
        "AstroBot shutting down.",
        parent_id=last_message_id
    )

    break
```

**Design Notes**

When the `/quit` command is received, the program invokes `send_message()` to notify the user that AstroBot is shutting down.

Unlike other commands, the program does not invoke an additional function to retrieve information to be supplied to send_message() function. Instead, it sends a static message indicating that the bot is terminating.

The `break` statement subsequently terminates the `while True` monitoring loop.

Because the monitoring loop is the final significant operation within `main()`, execution then returns from the main function.

As the program invokes `main()` directly at first level and has no subsequent instructions, the Python process normally terminates after the function returns.

This provides a controlled shutdown mechanism without requiring the administrator to manually terminate the Python process. It also allows the program to be terminated remotely through Webex without requiring direct access to the host system.

**Development Consideration**

The program does not currently implement a dedicated shutdown function or a comprehensive resource cleanup procedure.

It also does not include automatic recovery if the program terminates unexpectedly because of an unhandled exception.

Future improvements could include more advanced exception handling, shutdown logging and automatic restart functionality.

## 4. Testing and Development

Testing and Prototyping the fixes 

### Changes made during development

- **Configuration and Webex:** I moved API keys into environment-based settings with `.env` support. I updated command handling for the required slash commands and Webex group/team rooms. I also added API error logging and handling for Webex rate limits.
- **Request fixes:** The OpenWeather city lookup now sends the city as a normal string. I corrected the NASA key name so it matched the naming convention used by the rest of the program. The first screenshot shows this key correction.
- **New commands:** I added `/define` using a dictionary API and `/astronomy` using NASA's Astronomy Picture of the Day API. The astronomy result is sent to Webex as an image URL using their file-url parameter; the second screenshot shows development of that response.
- **ISS and weather:** `/iss` now converts the ISS timestamp from epoch time, reverse-geocodes its coordinates and requests weather for those same coordinates. `/weather <city>` looks up the city's coordinates, gets current weather for that location and formats the result. Both commands use the coordinate-based weather function. The weather output includes Celsius temperature, cloud cover, wind speed, a basic stargazing assessment and sunset time.
- **Other development:** I tried a NASA InSight Mars-weather command, but that API has been retired, so it was removed from the current code. I also changed the weather response to use separate lines. Some ISS heading labels have been added, but in the current code they need newline characters so they do not run into the text that follows.

### Screenshots and testing notes

The NASA key screenshot records a mismatch found while configuring the API key. I changed the key name so the code could look it up consistently.

![NASA API key correction](<Development Issues and Notes/Screenshot 2026-10-16 223918.png>)

The astronomy screenshot shows the APOD result being sent through the Webex file-message function.

![Astronomy command development](<Development Issues and Notes/Screenshot 2026-10-17 110133.png>)

The weather screenshot is an earlier test. It shows that the report could not assess stargazing when wind-gust data was unavailable. I changed the assessment to use cloud cover and wind speed instead, so it no longer depends on a gust value. If cloud cover or wind speed is missing, the assessment can still be unavailable.

![Earlier weather test showing unavailable gust data](<Development Issues and Notes/Screenshot 2026-10-19 122114.png>)

The ISS timestamp conversion, weather lookup at ISS coordinates, shared weather functions, sunset display and output formatting do not have screenshots here. They are described above based on the current code and the development history.

### Requirements still to check

The assignment appendix asks for polling every five seconds, while the current code waits ten seconds. The room list shows room name and ID, but not room type. Some API functions also assume response fields are present, so missing or malformed data is not handled safely in every case.



