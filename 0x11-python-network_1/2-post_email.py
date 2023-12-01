#!/usr/bin/python3
"""displays the value of the X-Request-Id found in the header of the res"""
from urllib import request, parse
from sys import argv

url = argv[1]
data = {'email': argv[2]}
data = parse.urlencode(data).encode('ascii')
req = request.Request(url, data)
with request.urlopen(req) as res:
    print("{}".format(res.read().decode('utf-8')))
