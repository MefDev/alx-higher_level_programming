#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests
url = 'https://alx-intranet.hbtn.io/status'


res = requests.get(url)
content = res.text
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(content), content))
