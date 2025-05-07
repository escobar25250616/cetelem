from flask import Flask, request, render_template

app = Flask(__name__)
messages = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", messages=messages)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data:
        messages.append(data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
