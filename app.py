from flask import Flask
import redis

app = Flask(__name__)

# Connection au service Redis (nom = service dans docker-compose)
r = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    r.incr("counter")
    return f"Visites : {r.get('counter').decode()}"

# N'exécute le serveur que si script lancé directement
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
