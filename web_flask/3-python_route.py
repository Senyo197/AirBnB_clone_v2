#!/usr/bin/python3
"""Falsk application creates several routes
"""
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route that displays 'C ' followed by the value of the text variable.

    Args:
        text (str): The text variable in the URL.

    Returns:
        str: C followed by the value of text (underscores replaced with spaces)
    """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Route that displays 'Python ' followed by the value of the text variable.
    The default value of text is 'is_cool'.

    Args:
        text (str): The text variable in the URL.

    Returns:
        str: Python followed by the value of text
        (underscores replaced with spaces).
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    """
    Main entry point of the application.

    Starts the Flask development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
