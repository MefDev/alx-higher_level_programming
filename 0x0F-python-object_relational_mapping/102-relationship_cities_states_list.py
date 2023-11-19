#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
# Usage: ./102-relationship_cities_states_list.py <mysql username> \
#                                                 <mysql password> \
#                                                 <database name>


def main():
    """lists all city objects"""
    # Start session
    session = Session()

    # Get the state
    states = session.query(State).order_by(State.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))


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
