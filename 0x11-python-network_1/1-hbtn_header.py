#!/usr/bin/python3
"""displays the value of the X-Request-Id found in the header of the res"""
from urllib import request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as res:
        print("{}".format(res.headers.get('X-Request-Id')))
