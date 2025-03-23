# database/models.py

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our models.
Base = declarative_base()


# --- User Table ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    real_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    # Removed the CheckConstraint that used the "~" operator for SQLite


# --- TripRequest Table ---
class TripRequest(Base):
    __tablename__ = "trip_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    budget = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    persons = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    duration = Column(Integer, nullable=False)  # Duration in days
    activities = Column(Text, nullable=True)


# --- Itinerary Table ---
class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    trip_request_id = Column(Integer, ForeignKey("trip_requests.id"), nullable=False)
    itinerary_info = Column(Text, nullable=False)  # Detailed itinerary info provided by the system
    traveller_details = Column(Text, nullable=True)  # Traveller details (e.g., JSON string with age, gender, gov_id)
