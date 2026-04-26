<!-- Mini Project 3: Web App -->

This project uses Flask to accept a place name and locate the nearest MBTA station. The app will show the coordinates, the station name, and its accessibility. A map will appear once the core features are complete.

<!-- Features -->
- Form where the user enters a place name
- Mapbox geocoding to get latitude/longitude
- MBTA API call to find nearest stop
- Results page showing stop name and accessibility
- Error handling for invalid locations

<!-- How to Run -->
1. Create a .env file with:
   MAPBOX_KEY=your_key_here
   MBTA_KEY=your_key_here

2. Install dependencies:
   pip install flask python-dotenv requests

3. Run the app:
   python app.py

4. Visit:
   http://127.0.0.1:5000/
