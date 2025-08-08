from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.getenv("gemini_api_key"))

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["Is there beach in trichy?"],
    config=types.GenerateContentConfig(
        temperature=0.2
    )
)

for chunk in response:
    print(chunk.text, end="")