#!/usr/bin/python3
"""displays the content of the res & post a req"""
import requests
from sys import argv

url = argv[1]
data = {'email': argv[2]}
res = requests.post(url, data)
print("{}".format(res.text))
