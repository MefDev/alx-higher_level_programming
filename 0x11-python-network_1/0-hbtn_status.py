#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as res:
    binary_content = res.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(binary_content), binary_content, binary_content.decode()
                  ))
