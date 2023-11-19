#!/usr/bin/python3
"""Insert California and San Fransisco to the DB"""
# Usage: ./100-relationship_states_cities.py <mysql username> \
#                                            <mysql password> \
#                                            <database name>


def main():
    """Inset city and state to DB using relationship"""
    # Start session
    session = Session()

    # save the state and city
    city = City(name="San Francisco")
    State(name='California').cities.append(city)
    session.add(city)
    session.commit()


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
