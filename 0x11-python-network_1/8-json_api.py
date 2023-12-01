#!/usr/bin/python3
"""Displays the body of the response (decoded in utf-8) & handle error"""
import requests
from sys import argv
if __name__ == "__main__":
    q = ""
    if (len(argv) == 1):
        q = ""
        print("No result")
    else:
        res = requests.get('http://0.0.0.0:5000/search_user', )
        if (len(res.json()) == 0):
            print('No result')
        try:
            if (len(argv) > 1):
                q = argv[1]
            for obj in res.json():
                if (obj['name'].startswith(q)):
                    print("[{}] {}".format(obj['id'], obj['name']))
                    exit()
            print('No result')
            
        except TypeError:
            print("Not a valid JSON")
