#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8) & handle error"""
import requests
from sys import argv
if __name__ == "__main__":
    data = {'q': argv[1] if len(argv) > 1 else ""}
    res = requests.get('http://0.0.0.0:5000/search_user', data=data)
    try:
        resp = res.json()
        if resp:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
