#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import MySQLdb
from sys import argv

# Arguments from the CLI
MY_USER, MY_PASS, MY_DB = argv[1], argv[2], argv[3]


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    states = cur.fetchall()
    # Get the states
    for state in states:
        print(state)
