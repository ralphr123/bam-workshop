from dotenv import load_dotenv; load_dotenv()
import os
from flask import Flask

message = os.getenv('HELLO_WORLD')

app = Flask(__name__)

# Allow frontend origin to make requests
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response

@app.route('/')
def hello():
    return message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)