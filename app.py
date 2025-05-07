from flask import Flask, request

app = Flask(__name__)
messages = []

@app.route("/", methods=["GET"])
def index():
    return "<h1>Serveur Flask en ligne</h1><p>Le webhook Telegram est prêt.</p>"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data:
        messages.append(data)
        print("Message reçu :", data)  # Pour debug Render (logs)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
