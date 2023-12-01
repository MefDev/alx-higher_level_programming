#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests
url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    res = requests.get(url)
    content = res.text
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(content), content))
