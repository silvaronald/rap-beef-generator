from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Use the API
response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL"),
    config=types.GenerateContentConfig(
        system_instruction="You are a famous United States rapper. Your job is to destroy your enemy named Drake."
    ),
    contents="Write a one-verse rap diss with 4 lines maximum."
)

print(response.text)
