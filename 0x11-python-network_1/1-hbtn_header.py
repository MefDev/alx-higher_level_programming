#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header of the response"""
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as res:
    print("{}".format(res.headers.get('X-Request-Id')))
