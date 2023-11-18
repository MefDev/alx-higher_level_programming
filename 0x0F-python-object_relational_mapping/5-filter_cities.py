#!/usr/bin/python3
"""Takes in the name of a state as an args & lists all cities of that state"""
# Lists the filtered states from the database hbtn_0e_0_usa.
# Usage: ./5-filter_cities.py <mysql username> \
#                             <mysql password> \
#                             <database name> \
#                             <state name>


def main(args):
    """Select filtered states from MY_DB"""

    # Arguments from the CLI
    MY_USER, MY_PASS, MY_DB, STATE_NAME = args[1], args[2], args[3], args[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    query = (
        "SELECT cities.name \
         FROM states JOIN cities \
         ON states.id=cities.state_id AND states.name=%s \
         ORDER BY cities.state_id ASC")
    cur.execute(query, (STATE_NAME,))
    states = cur.fetchall()
    # Get the states
    if (states):
        for index, state in enumerate(states):
            if len(states) - 1 != index:
                print(list(state)[0], end=", ")
            else:
                print(list(state)[0])
    else:
        print("")


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main(argv)
