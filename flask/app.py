from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello Flask <h1>This is main page</h1>"

@app.route("/<name>")
def home(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("main"))
if __name__ == "__main__":
    app.run()
