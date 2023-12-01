#!/usr/bin/python3
"""Get the id of a usr from github"""
import requests
from sys import argv
auth = (argv[1], argv[2])
res = requests.get('https://api.github.com/user', auth=auth)
print(res.json().get('id'))
