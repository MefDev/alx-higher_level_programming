#!/usr/bin/python3
"""List 10 latest commits"""

if __name__ == "__main__":
    import requests

    from sys import argv
    query_max = 'per_page=10'
    owner, repo = argv[1], argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?'

    list_of_commiters = requests.get(url + query_max)
    for committer in list_of_commiters.json():
        sha = committer.get('sha')
        name = committer.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
