#!/usr/bin/python3
"""Print all City object from DB"""
# Usage: ./100-relationship_states_cities.py <mysql username> \
#                                            <mysql password> \
#                                            <database name>


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
    # Start session
    session = Session()

    # Get the state
    san_francisco = City(name="San Francisco")
    california = State(name='California')
    # save the state and city
    session.add(san_francisco, california)
    session.commit()
    session.close()
