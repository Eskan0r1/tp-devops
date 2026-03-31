from flask import Flask
import redis
import os
import time

app = Flask(__name__)

# Configuration Redis depuis les variables d'environnement
REDIS_HOST = os.environ.get("REDIS_HOST", "devops-redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))




def get_redis_connection():
    r = None
    for attempt in range(5):
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
            r.ping()
            print(f"Connecté à Redis sur {REDIS_HOST}:{REDIS_PORT}")
            return r
        except redis.exceptions.ConnectionError:
            print(f"Redis non disponible, tentative {attempt+1}/5, attente 2s...")
            time.sleep(2)
    return None

# Connexion Redis globale
r = get_redis_connection()

@app.route("/")
def home():
    if r:
        if not r.exists("counter"):
            r.set("counter", 0)
        r.incr("counter")
        count = r.get("counter").decode()
        return f"Visites : {count}"
    else:
        return "Redis non disponible", 500

@app.route("/hello")
def hello():
    return "Hello DevOps"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
