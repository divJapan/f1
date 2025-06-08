import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dati da esporre
f1_data = {}

@app.route("/aggiorna", methods=["POST"])
def aggiorna():
    global f1_data
    f1_data = request.json
    return "", 204

@app.route("/dati", methods=["GET"])
def dati():
    return jsonify(f1_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
