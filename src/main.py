from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_api_key"))

# One-shot example: show 1 QA pair, then ask a new one
prompt = """
Question: Which is the most beautiful beach in India?
Answer: Radhanagar Beach in the Andaman Islands

Question: Which is the most beautiful beach in the world?
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt],
    config=types.GenerateContentConfig(
        temperature=0.3
    )
)

print(response.text)
