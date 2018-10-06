import requests
import doctest


def fetch_url(url):
    return requests.get(url).json()


def get_titles(url):
    _json = fetch_url(url)
    for elem in _json['results']:
        yield elem['translation']['title']


def my_sum(a, b):
    """
    >>> my_sum(5, 3)
    8
    """
    return a + b


def my_div(a, b):
    """
    >>> my_div(1,2)
    0.5

    >>> my_div(1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b

if __name__ == '__main__':
    doctest.testmod()
