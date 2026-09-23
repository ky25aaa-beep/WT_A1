import logging, ngrok, os
import time
MY_STATIC_DOMAIN = "busybody-refreeze-grill.ngrok-free.dev"

NGROK_AUTHTOKEN = "3JP6B9pa5HITY8nQhDjkGTmwwzG_4FfkP2aJBKQvYzKXG2jsR"
 
logging.basicConfig(level=logging.INFO)
listener = ngrok.forward("localhost:8080", authtoken=NGROK_AUTHTOKEN,     domain=MY_STATIC_DOMAIN)

try:
    # Keep script alive indefinitely
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Shutting down tunnel...")
    listener.close()