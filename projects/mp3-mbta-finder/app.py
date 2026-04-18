from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Mini Project 3 — Milestone 0"

if __name__ == "__main__":
    app.run(debug=True)
