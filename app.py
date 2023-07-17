from flask import Flask
from src.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("inside index function")
    return "welcome to flask"

if __name__ == '__main__':
    logging.info('Testing second method of logging')
    app.run(debug=True)