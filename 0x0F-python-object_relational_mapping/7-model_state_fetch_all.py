#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_us"""
# Lists the filtered states from the database hbtn_0e_0_usa.
# Usage: ./2-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>


def main():
    """List states"""

    # Start session
    session = Session()

    # Get the states
    states = session.query(State).order_by(State.id)
    [print("{}: {}".format(state.id, state.name)) for state in states]


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
