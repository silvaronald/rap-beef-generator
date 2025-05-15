from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_diss_rap(user_input: str) -> str:
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        config=types.GenerateContentConfig(
            system_instruction="You are a famous United States rapper. Your job is to destroy your enemy named Drake using a rap diss-track."
        ),
        contents=f"Write a rap diss against Drake. You have to meet these requirements: {user_input}"
    )

    return response.text
