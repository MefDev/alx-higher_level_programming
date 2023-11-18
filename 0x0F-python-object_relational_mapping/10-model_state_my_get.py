#!/usr/bin/python3
"""print the State object with the name passed as argument"""
# Usage: ./10-model_state_my_get.py <mysql username> \
#                                   <mysql password> \
#                                   <database name>
#                                   <state name>


def main(args):
    """Get a state"""

    # Start session
    session = Session()
    # GET args from CLI
    STATE_NAME = args[4]
    # Get the states
    states = session.query(State).filter(State.name == STATE_NAME).all()
    if (states):
        [print("{}".format(state.id)) for state in states]
    else:
        print("Not found")


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
    main(argv)
