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

    if message == "FACEBOOK_WELCOME":
        Messenger().respond_user(sender_id, "Digite uma palavra para pesquisar por notícias relacionadas!")
    else:
        Messenger().respond_user(sender_id, __news(message))
    return "ok"

def __news(message):
    globo = Globo()
    news = globo.find_news(message)
    return globo.format_for_messenger(news)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
