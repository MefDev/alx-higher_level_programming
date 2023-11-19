#!/usr/bin/python3
"""Print all City object from DB"""
# Usage: ./14-model_city_fetch_by_state.py <mysql username> \
#                                          <mysql password> \
#                                          <database name>


def main():
    """Add a state"""

    # Start session
    session = Session()

    # Get the state
    state_and_cities = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id)

    # Print each state and city
    for state, city in state_and_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # configure the setup
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    main()
