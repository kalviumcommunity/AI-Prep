from google import genai
import os
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("gemini_api_key"))

prompt = """
Question: Which is the most beautiful beach in India?
Answer: Radhanagar Beach in the Andaman Islands

Question: Which is the most beautiful beach in Thailand?
Answer: Maya Bay on Ko Phi Phi Leh

Question: Which is the most beautiful beach in Australia?
Answer: Whitehaven Beach in the Whitsundays

Question: Which is the most beautiful beach in Greece?
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt],
    config=types.GenerateContentConfig(
        temperature=0.3
    )
)
print(response.text)
