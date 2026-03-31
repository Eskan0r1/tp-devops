from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("MESSAGE", "Hello Default")
    return message

# N’exécute pas le serveur si c’est importé (pour la CI)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
