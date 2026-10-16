# Code Review and Explanation, along with development notation and review. 
## Table of Contents


## Function Names and purposes 



# Functions and Their Purposes

| Function Name | Description | Invoked By | Invokes |
|---|--------|---|---|
| `handle_api_error()` | Serve Messages to webex, and save them to an error file (prevents errors from causing application failures that result in system downtime) | `get_rooms()`, `get_latest_message()`, `send_message()`, `get_city_coordinates()`, `get_weather()`, `reverse_geocode()`, `get_iss_location()`, `get_word_definition()`, `send_message_file()`, `astronomy_picture_day()`, `get_mars_weather()`, `handle_api_error()` | `send_message()`, `handle_api_error()` |
| `get_api_keys()` | Retrieve apikeys from .env/system if required keys arent present retrieve them from the systems administrator that runs the programme| `main()` | — |
| `get_rooms()` | Via interacting with the webex api it retrieves the rooms where the bot has access to i | `main()` | `handle_api_error()` |
| `print_rooms()` | displays the rooms the webex bot is present in to the system admin | `main()` | — |
| `select_room()` | handles selecting the active sessions's room, this dictates the roomid to the rest of the programe and restricts the bots interactions, message sending and retrieval to that specific messaging space| `main()` | — |
| `get_latest_message()` | Via interacting with the webex api it retrieves the latest 100 messages that mention (i.e tag @webex_bot_name.| `main()` | `send_message()`, `handle_api_error()` |
| `send_message()` | Via interacting with the webex api it sends a message as a reply to the previous message that tagged the bot and invoked a command| `main()`, `get_latest_message()`, `handle_api_error()` | `handle_api_error()` |
| `get_city_coordinates()` |Via interacting with the openweathermap api it retrieves the latitude and longitude of the queried city  | `get_weather()` | `handle_api_error()` |
| `get_weather()` | Via interacting with the oopenweathermap api it retrieves the weather information for the long and lat provided to it by the get_city_coordinates api| `main()` | `get_city_coordinates()`, `handle_api_error()` |
| `reverse_geocode()` | It is provided with lat and long of the area the IIS Sits above and by utilising the openweathermap api it retrieves the city/area that rests below that location. | `get_iss_location()` | `handle_api_error()` |
| `get_iss_location()` | Via utilising the IIS api provided by nasa it determines the lat and long of the area the iis is positioned above at the last moment it reported its location to nasa/was located via satelite | `main()` | `reverse_geocode()`, `handle_api_error()` |
| `get_word_definition()` | Via utilising the freedictionaryapi it retrieves the highest rated definition for the word provided in the query | `main()` | `handle_api_error()` |
| `send_message_file()` |Via utilising the same api as send_message it is able to send files over to the message that invoked the command as a reply (this is only used for image files) | `main()` | `handle_api_error()` |
| `astronomy_picture_day()` | Via utilising the astronomy api provided by nasa it retrieves the high definition astronomy picture of the day and its title| `main()` | `handle_api_error()` |
| `get_mars_weather()` | it retrieves the weather on mars (currently nonfunctional)| `main()` | `handle_api_error()` |
| `main()` | Main Sequence of code to intiialise the program| Module-level entry point | `get_api_keys()`, `get_rooms()`, `print_rooms()`, `select_room()`, `get_latest_message()`, `send_message()`, `get_weather()`, `get_iss_location()`, `get_mars_weather()`, `get_word_definition()`, `astronomy_picture_day()`, `send_message_file()` |
