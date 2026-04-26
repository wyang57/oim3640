from flask import Flask, render_template, request
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
    key = os.environ.get('MBTA_KEY')
    url = "https://api-v3.mbta.com/stops"
    params = {
        "api_key": key,
        "filter[latitude]": lat,
        "filter[longitude]": lng,
        "sort": "distance",
        "page[limit]": 1
    }
    r = requests.get(url, params=params).json()
    try:
        stop = r["data"][0]["attributes"]
        name = stop["name"]
        access = stop["wheelchair_boarding"]
        return name, access
    except:
        return None

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/result")
def result():
    place = request.form.get("place")
    coords = get_coordinates(place)

    if coords is None:
        return render_template("result.html", error="Place not found.")

    lat, lng = coords
    stop = get_nearest_stop(lat, lng)

    if stop is None:
        return render_template("result.html", error="No nearby stops found.")

    name, access = stop
    return render_template("result.html",
                           place=place,
                           stop=name,
                           access=access,
                           lat=lat,
                           lng=lng)

if __name__ == "__main__":
    app.run(debug=True)
