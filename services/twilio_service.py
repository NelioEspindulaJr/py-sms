import os
import json

from twilio.rest import Client


class TwilioService:
    def __init__(self) -> None:
        self.__client = Client(
            account_sid=os.environ["TWILIO_ACCOUNT_SID"],
            password=os.environ["TWILIO_AUTH_TOKEN"],
        )

        self.__phone_number = os.environ["TWILIO_PHONE_NUMBER"]

    async def send_verification_code(self, to: str, verification_code: str):
        message_body = "Seu código de verificação é: %f. " % verification_code

        message = await self.__client.messages.create_async(
            to=to, from_=self.__phone_number, body=message_body
        )

        return message.sid
