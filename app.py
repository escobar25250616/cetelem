from flask import Flask, request
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
    html = "<h1>Messages reçus :</h1><ul>"
    for m in messages:
        try:
            text = m['message']['text']
            user = m['message']['from']['first_name']
            html += f"<li><b>{user}</b> : {text}</li>"
        except:
            html += "<li>(message non texte)</li>"
    html += "</ul>"
    return html

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data:
        messages.append(data)
        # Enregistrer dans messages.json
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        print("Message reçu :", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
