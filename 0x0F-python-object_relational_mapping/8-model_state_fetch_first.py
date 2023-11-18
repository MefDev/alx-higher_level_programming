#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_us"""
# Usage: ./8-model_state_fetch_first.py <mysql username> \
#                                       <mysql password> \
#                                       <database name>


def main():
    """List states"""

    # Start session
    session = Session()

    # Get the states
    first_state = session.query(State).first()
    if (first_state):
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # configure the setup
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    main()
