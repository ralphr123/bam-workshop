# Load environment variables
from dotenv import load_dotenv; load_dotenv()

# Flask is used to accept HTTP requests
from flask import Flask

# Import exercise modules
from _EDIT_THESE_FILES.exercise1 import sendMessage as Exercise1__sendMessage
from _EDIT_THESE_FILES.exercise2 import Chat as Exercise2__Chat
from _EDIT_THESE_FILES.exercise3 import Chat as Exercise3__Chat
from _EDIT_THESE_FILES.exercise4 import system_msg as Exercise4__system_msg

app = Flask(__name__)

# Allow frontend origin to make requests
@app.after_request
def afterRequest(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response

@app.route('/exercise1/<message>')
def exercise1(message: str):
    try:
        res = Exercise1__sendMessage(message)

        return { 'response': res }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
        return {}

@app.route('/exercise2/<message>')
def exercise2(message: str):
    try:
        chat = Exercise2__Chat()

        res = chat.sendMessage(message)

        return { 'response': res }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
        return {}

@app.route('/exercise3/<prompt>/<message>')
def exercise3(prompt: str, message: str):
    try:
        chat = Exercise3__Chat(prompt)

        res = chat.sendMessage(message)

        return { 'response': res }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
        return {}

@app.route('/exercise4/<maze_code>')
def exercise4(maze_code: str):
    try:
        chat = Exercise3__Chat(Exercise4__system_msg)

        res = chat.sendMessage(maze_code)

        return { 'instructions': res.splitlines() }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
        return {}

@app.route('/')
def helloWorld():
    return { 'text': 'Hello world!' }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)
