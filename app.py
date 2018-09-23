import os

from flask import Flask, jsonify, request


verify_token = os.getenv("MESSENGER_VERIFY_TOKEN", "blablabla")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def dale_gif():
    if request.args.get("hub.verify_token") == verify_token:
        return request.args.get("hub.challenge")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
