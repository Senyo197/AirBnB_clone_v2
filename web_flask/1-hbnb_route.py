#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!'

    Returns:
        str: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB'

    Returns:
        str: HBNB
    """
    return 'HBNB'


if __name__ == '__main__':
    """
    Main entry point of the application.

    Starts the Flask development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
