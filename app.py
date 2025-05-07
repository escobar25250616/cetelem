from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = "messages.json"

# Charger les anciens messages s’ils existent
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
else:
    messages = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", messages=messages)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data:
        messages.append(data)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        print("Message reçu :", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
