from hashlib import new
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('X_TOKEN', 'RobertRobert')  # Use environment variable

# # GET: read all messages
# data = requests.get(
#     'https://oim.108122.xyz/messages',
#     headers={'X-Token': TOKEN}
# ).json()
# for msg in data:
#     print(msg)

# # POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#               json={'message': 'Hello from Robert!'},
#               headers={'X-Token': TOKEN})


# API_KEY = os.getenv('OPENWEATHER_API_KEY')
# if API_KEY:
#     url = (f'https://api.openweathermap.org/data/2.5/weather'
#            f'?q=Boston&appid={API_KEY}&units=imperial')
#     response = requests.get(url)
#     data = response.json()
#     if response.status_code == 200:
#         print(f"Boston: {data['main']['temp']}°F")
#     else:
#         print(f"API Error: {response.status_code}")
#         print(f"Message: {data.get('message', 'Unknown error')}")
#         if response.status_code == 401:
#             print("Please get a valid API key from https://openweathermap.org/api")
# else:
#     print("OpenWeather API key not found. Please set OPENWEATHER_API_KEY in .env file")

# OpenAI API: Generate a bedtime story
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}]
)

print(response.choices[0].message.content)

