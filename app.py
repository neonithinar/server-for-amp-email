# Required imports
import os
from flask import Flask
from time import time
from database import get_data, write_data

# from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

milliseconds = int(time() * 1000)


@app.route('/')
@app.route('/home')
def home():
    return "<h1> hello world </h1>"


@app.route('/read', methods=['GET'])
def read_data():
    try:
        data = get_data()
        return data
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/write', methods=['GET', 'POST'])
def post_data():
    """
        posts data to firebase db
    """
    # data = {"email": email,
    #         "message": message,
    #         "timestamp": milliseconds}
    response = write_data()
    return response



port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(debug=True, port=port)
