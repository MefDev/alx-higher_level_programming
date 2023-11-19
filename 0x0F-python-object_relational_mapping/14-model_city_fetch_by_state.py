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
    state_and_cities = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).order_by(City.id)
    if (state_and_cities):
        # Print each state and city
        for state_name, city_id, city_name in state_and_cities:
            print("{}: ({}) {}".format(state_name, city_id, city_name))


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
