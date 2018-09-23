import os

from flask import Flask, request

from messenger import Messenger
from globo import Globo


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def bot():
    if request.method ==  "GET":
        return Messenger.challenge(
            request.args.get("hub.verify_token"),
            request.args.get("hub.challenge")
        )

    entry = request.json.get("entry")
    sender_id, message = Messenger.sender_id_and_message(entry)

    globo = Globo()
    news = globo.find_news(message)
    formatted_news = globo.format_for_messenger(news)

    Messenger().respond_user(sender_id, formatted_news)

    return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
