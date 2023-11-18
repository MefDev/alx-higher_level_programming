#!/usr/bin/python3
"""Delete all State objects with a name containing the letter a"""
# Usage: ./13-model_state_delete_a.py <mysql username> \
#                                     <mysql password> \
#                                     <database name>


def main():
    """Add a state"""

    # Start session
    session = Session()

    # Get the state
    states = session.query(State).filter(State.name.like('%a%')).all()
    if (states):
        # delete each state that correspond to the condition
        [session.delete(state) for state in states]
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
