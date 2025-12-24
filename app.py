from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def get_states():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
