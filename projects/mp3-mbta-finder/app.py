from flask import Flask

app = Flask(__name__)

# Placeholder API Functions

def get_coordinates(place):
    return None

def get_nearest_stop(lat, lng):
    return None

#Routes

@app.get("/")
def index():
    return "Mini Project 3 — Milestone 0"

if __name__ == "__main__":
    app.run(debug=True)
