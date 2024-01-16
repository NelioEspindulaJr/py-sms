from flask import Flask
from dotenv import load_dotenv


app = Flask(__name__)


@app.route("/send-message/<to_phone_number>")
def send_message(to_phone_number):
    return "Hello, world!"


if __name__ == "__main__":
    load_dotenv()
    app.run()
