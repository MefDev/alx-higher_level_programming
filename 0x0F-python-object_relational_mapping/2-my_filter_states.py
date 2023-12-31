#!/usr/bin/python3
"""Get the filtered states from the database using the CLI arguments"""
# Lists the filtered states from the database hbtn_0e_0_usa.
# Usage: ./2-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>


def main(args):
    """Select filtered states from MY_DB"""

    # Arguments from the CLI
    MY_USER, MY_PASS, MY_DB, STATE_NAME = args[1], args[2], args[3], args[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}%'"
             ).format(STATE_NAME)
    cur.execute(query)
    states = cur.fetchall()
    # Get the states
    [print(state) for state in states]


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main(argv)
