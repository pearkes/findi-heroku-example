import os

from datetime import datetime
from findi import FindMyIPhone
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This will raise an exception of they are not in the environment.
APPLE_EMAIL = os.environ["APPLE_EMAIL"]
APPLE_PASSWORD = os.environ["APPLE_PASSWORD"]
DATABASE_URL = os.environ["DATABASE_URL"]

# Sqlachemy Engine
engine = create_engine(DATABASE_URL)

# Sqlalchemy Base Class
Base = declarative_base()

# Sqlalchemy Session
Session = sessionmaker(bind=engine)
# We'll use db later for database operations.
db = Session()


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    latitude = Column(String, )
    longitude = Column(String)
    date = Column(String, default=datetime.utcnow,
                  onupdate=datetime.utcnow)

    def __repr__(self):
        return "<Location('%s','%s', '%s')>" % (self.latitude, self.longitude, self.date)


def store_location():
    "Fetches an iPhone location from the Apple API and creates a Location Object"
    iphone = FindMyIPhone(APPLE_EMAIL, APPLE_PASSWORD)
    iphone_location = iphone.locate()

    location = Location()
    location.latitude = iphone_location.get('latitude')
    location.longitude = iphone_location.get('longitude')
    db.add(location)
    # Persist to the database
    db.commit()
    return location

if __name__ == "__main__":
    location = store_location()
    print "Succesfully stored: %s" % location
