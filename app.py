from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("MESSAGE", "Hello Default")
    return message

app.run(host="0.0.0.0", port=5000)
