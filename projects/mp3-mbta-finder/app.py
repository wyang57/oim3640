from flask import Flask
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

def get_coordinates(place):
    key = os.environ.get('MAPBOX_KEY')
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json"
    params = {"access_token": key, "limit": 1}
    r = requests.get(url, params=params).json()
    try:
        coords = r["features"][0]["geometry"]["coordinates"]
        lng, lat = coords
        return lat, lng
    except:
        return None


def get_nearest_stop(lat, lng):
    return None

@app.get("/test")
def test():
    result = get_coordinates("Boston")
    return str(result)


@app.get("/")
def index():
    return "Mini Project 3 — Milestone 0"

if __name__ == "__main__":
    app.run(debug=True)
