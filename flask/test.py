from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello <h1>Flask</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirecdt(url_for('homepage'))
if __name__ == "__main__":
    app.run()