#!/usr/bin/python3
"""List 10 latest commits"""

if __name__ == "__main__":
    import requests
    from sys import argv

    owner = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo)

    list_of_commiters = requests.get(url)
    i = 10
    for committer in list_of_commiters.json():
        if (i > 0):
            sha = committer.get('sha')
            name = committer.get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
            i -= 1
