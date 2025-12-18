from flask import Flask
app = Flask(__name__)

@app.route("/")
def ok():
    return {"status": "ok"}

app.run(host="0.0.0.0", port=8080)
