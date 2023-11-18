#!/usr/bin/python3
"""Get the filtered states from the database using the CLI arguments"""
# Lists the filtered states from the database hbtn_0e_0_usa.
# Usage: ./4-cities_by_state.py <mysql username> \
#                             <mysql password> \
#                             <database name>


def main(args):
    """Select filtered states from MY_DB"""

    # Arguments from the CLI
    MY_USER, MY_PASS, MY_DB = args[1], args[2], args[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name \
         FROM states JOIN cities \
         ON states.id=cities.state_id ORDER BY cities.state_id ASC")
    cur.execute(query)
    states = cur.fetchall()
    # Get the states
    [print(state) for state in states]


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    main(argv)
