from flask import Flask, request

app = Flask(__name__)
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
        print("Message reçu :", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
