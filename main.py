from dotenv import load_dotenv; load_dotenv()
import os

def main():
  message = os.getenv('MY_ENV_VAR', 'Environment variable not set')
  print(message)

if __name__ == "__main__":
  main()