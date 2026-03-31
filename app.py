from flask import Flask
import redis

app = Flask(__name__)

# Connexion au service Redis (nom = service dans docker-compose)
try:
    r = redis.Redis(host="redis", port=6379)
    r.ping()  # Vérifie que Redis est joignable
except redis.exceptions.ConnectionError:
    r = None

@app.route("/")
def home():
    if r:
        # Initialise le compteur si nécessaire
        if not r.exists("counter"):
            r.set("counter", 0)
        r.incr("counter")
        count = r.get("counter").decode()
        return f"Visites : {count}"
    else:
        return "Redis non disponible", 500

# N'exécute le serveur que si script lancé directement
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
