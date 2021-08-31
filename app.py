from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def default():
    return "Working"



if(__name__ == "__main__"):
    app.run(debug=True)