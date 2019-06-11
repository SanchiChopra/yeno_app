from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/harry")
def harry():
    return "Hello Harry!"

app.run(debug=True)
