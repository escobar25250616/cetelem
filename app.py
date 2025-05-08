from flask import Flask, request, render_template, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "messages.json"

# Charger les anciens messages s’ils existent
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            messages = json.load(f)
        except json.JSONDecodeError:
            messages = []
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
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/suivant", methods=["POST"])
def suivant():
    identifiant = request.form.get("identifiant")
    remember = request.form.get("remember") == "on"
    # Ici, tu peux traiter les données comme tu veux
    print(f"Identifiant reçu : {identifiant}, Remember: {remember}")
    return render_template("suivant.html", identifiant=identifiant, remember=remember)
