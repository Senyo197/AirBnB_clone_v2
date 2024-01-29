#!/usr/bin/python3
"""Falsk application creates several routes
"""
from flask import Flask, render_template

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
    return 'C {}'.format(text.replace('_', ' '))


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
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route that displays 'n is a number' only if n is an integer.

    Args:
        n (int): The number variable in the URL.

    Returns:
        str: 'n is a number' if n is an integer, otherwise a 404 error.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page only if n is an integer.
    The HTML page includes an H1 tag with the content 'Number:
    n' inside the BODY tag.

    Args:
        n (int): The number variable in the URL.

    Returns:
        str: HTML page with 'Number: n' in an H1 tag inside the BODY tag,
        or a 404 error.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return "Not Found", 404


if __name__ == '__main__':
    """
    Main entry point of the application.

    Starts the Flask development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
