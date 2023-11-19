#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""
# Usage: ./101-relationship_states_cities_list.py <mysql username> \
#                                                 <mysql password> \
#                                                 <database name>


def main():
    """lists all State objects"""
    # Start session
    session = Session()

    # Get the state and city
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    from sys import argv
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # configure the setup
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    main()
