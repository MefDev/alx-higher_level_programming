#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8) & handle error"""
import requests
from sys import argv
if __name__ == "__main__":
    data = {'q': "" if len(argv) == 1 else argv[1]}
    res = requests.get('http://54.237.23.212:5000/search_user', data=data)
    try:
        if res.json():
            resp = res.json()
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
