#!/usr/bin/python3
"""List 10 latest commits"""

if __name__ == "__main__":
    import requests
    from sys import argv

    owner = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
        owner, repo)

    list_of_commiters = requests.get(url)

    for committer in list_of_commiters.json():
        sha = committer.get('sha')
        name = committer.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
