#!/usr/bin/python3
"""Get the filtered states from the database used in the CLI"""
# Lists the filtered states from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>


def main(args):
    """Select filtered states from MY_DB"""

    # Arguments from the CLI
    MY_USER, MY_PASS, MY_DB = args[1], args[2], args[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE (ASCII(LEFT(name, 1)) = 78)"
    cur.execute(query)
    states = cur.fetchall()
    # Get the states
    [print(state) for state in states]


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main(argv)
