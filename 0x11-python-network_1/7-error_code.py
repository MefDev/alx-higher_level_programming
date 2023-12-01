#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8) & handle error"""
import requests
from sys import argv


url = argv[1]
res = requests.get(url)
if (res.status_code >= 400):
    print("Error code: {}".format(res.status_code))
else:
    print("{}".format(res.text))
