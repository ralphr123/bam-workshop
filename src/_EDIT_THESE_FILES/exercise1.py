# Load environment variables from .env
from dotenv import load_dotenv; load_dotenv()

# Fetch environment variables from .env
import os

# OpenAI Python SDK to allow us to make requests to GPT
import openai

# Store OpenAI environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def sendMessage(message: str) -> str:
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[{'role': 'user', 'content': message}],
        temperature=0
    )

    return res['choices'][0]['message']['content']