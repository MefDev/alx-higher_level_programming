#!/usr/bin/python3
"""script that adds the State object “Louisiana to DB"""
# Usage: ./11-model_state_insert.py <mysql username> \
#                                   <mysql password> \
#                                   <database name>


def main(args):
    """Add a state"""

    # Start session
    session = Session()

    # add a state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    # Get the state
    states = session.query(State).filter(State.name == "Louisiana").all()
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
