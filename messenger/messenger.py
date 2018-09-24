import os

import requests


class Messenger:

    MESSENGER_VERIFY_TOKEN = os.getenv("MESSENGER_VERIFY_TOKEN")
    MESSENGER_PAGE_ACCESS_TOKEN = os.getenv("MESSENGER_PAGE_ACCESS_TOKEN")
    MESSENGER_URL = "https://graph.facebook.com/v2.6/me/messages?access_token=" + MESSENGER_PAGE_ACCESS_TOKEN

    def respond_user(self, sender_id, message):
        requests.post(
            self.MESSENGER_URL,
            json={
                "messaging_type": "RESPONSE",
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": message
                }
            }
        )

    @staticmethod
    def sender_id_and_message(entry):
        for message in entry:
            messaging = message["messaging"][0]
            if messaging.get("postback"):
                return (
                    messaging["sender"]["id"],
                    messaging["postback"]["payload"]
                )
            return (
                messaging["sender"]["id"],
                messaging["message"]["text"]
            )

    @classmethod
    def challenge(cls, hub_verify_token, hub_challenge):
        if hub_verify_token == cls.MESSENGER_VERIFY_TOKEN:
            return hub_challenge
