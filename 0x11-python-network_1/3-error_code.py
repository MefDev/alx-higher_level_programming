#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8) & handle error"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

try:
    url = argv[1]
    with request.urlopen(url) as res:
        print("{}".format(res.read().decode("utf-8")))

except HTTPError as e:
    print("Error code: {}".format(e.status))
