#!/usr/bin/python3
"""Changes the name of a State object"""
# Usage: ./11-model_state_insert.py <mysql username> \
#                                   <mysql password> \
#                                   <database name>


def main():
    """Add a state"""

    # Start session
    session = Session()

    # Get the state
    states = session.query(State).filter(State.id == 2).all()
    if (states):
        for state in states:
            state.name = "New Mexico"

    # save
    session.commit()


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
