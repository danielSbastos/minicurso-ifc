import os

from flask import Flask, request

from messenger import Messenger


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def bot():
    if request.method ==  "GET":
        return Messenger.challenge(
            request.args.get("hub.verify_token"),
            request.args.get("hub.challenge")
        )

    Messenger().respond_user(request.json.get("entry"))
    return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
