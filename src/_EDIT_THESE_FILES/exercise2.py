# Load environment variables from .env
from dotenv import load_dotenv; load_dotenv()

# Fetch environment variables from .env
import os

# OpenAI Python SDK to allow us to make requests to GPT
import openai

# Store OpenAI environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

class Chat:
	def __init__(self):
		self.messages = []

	def sendMessage(self, message: str) -> str:
		self.messages.append({'role': 'user', 'content': message})

		res = openai.ChatCompletion.create(
			model='gpt-3.5-turbo-16k',
			messages=self.messages,
			temperature=0
		)

		message = res['choices'][0]['message']['content']

		self.messages.append({'role': 'assistant', 'content': message})

		return message

if __name__ == '__main__':
	print("Exercise 2 optional test area.")
