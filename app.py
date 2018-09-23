import os

import requests
from flask import Flask, request

MESSENGER_VERIFY_TOKEN = os.getenv("MESSENGER_VERIFY_TOKEN")
MESSENGER_PAGE_ACCESS_TOKEN = os.getenv("MESSENGER_PAGE_ACCESS_TOKEN")
MESSENGER_URL = "https://graph.facebook.com/v2.6/me/messages?access_token=" + MESSENGER_PAGE_ACCESS_TOKEN

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def bot():
    if request.method == "GET":
        return __challenge(request)
    else:
        __answer_user(request)
        return "ok"

def __challenge(request_fb):
    if request_fb.args.get("hub.verify_token") == MESSENGER_VERIFY_TOKEN:
        return request_fb.args.get("hub.challenge")

def __answer_user(request_fb):
    requests.post(
        MESSENGER_URL,
        json={
            "messaging_type": "RESPONSE",
            "recipient": {
                "id": __sender_id(request_fb)
            },
            "message": {
                "text": "hello, world!"
            }
        }
    )

def __sender_id(request_fb):
    for entry in request_fb.json["entry"]:
        return entry["messaging"][0]["sender"]["id"]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
