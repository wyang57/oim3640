# pip install openai
# conda install openai

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}]
)

print(response.output_text)

