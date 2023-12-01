#!/usr/bin/python3
"""displays the value of the X-Request-Id found in the header of the res"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    print("{}".format(res.headers['X-Request-Id']))
