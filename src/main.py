from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_api_key"))

# User's input (could come from your app, chatbot, or database)
place = "Thailand"  
question = f"Which is the most beautiful beach in {place}?"

# Dynamic prompt
prompt = f"""
Question: Which is the most beautiful beach in India?
Answer: Radhanagar Beach in the Andaman Islands

Question: {question}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt],
    config=types.GenerateContentConfig(
        temperature=0.3
    )
)

print(response.text)
