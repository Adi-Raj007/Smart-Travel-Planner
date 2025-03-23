from pydantic import BaseModel, constr
from datetime import date
from typing import Optional

# --- Schemas for User ---
class UserCreate(BaseModel):
    username: constr(regex=r'^[A-Za-z0-9_]+$')  # Username must match regex.
    real_name: str  # The user's full, real name.
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    real_name: str
    email: str

    class Config:
        orm_mode = True

# --- Schemas for TripRequest ---
class TripRequestCreate(BaseModel):
    user_id: int
    budget: int
    location: str
    persons: int
    start_date: date  # Pydantic will parse date strings in 'YYYY-MM-DD' format.
    duration: int     # Duration in days.
    activities: Optional[str] = None

class TripRequestResponse(BaseModel):
    id: int
    user_id: int
    budget: int
    location: str
    persons: int
    start_date: date
    duration: int
    activities: Optional[str] = None

    class Config:
        orm_mode = True

# --- Schemas for Itinerary ---
class ItineraryCreate(BaseModel):
    trip_request_id: int
    itinerary_info: str
    traveller_details: Optional[str] = None  # Can store JSON details about travellers.

class ItineraryResponse(BaseModel):
    id: int
    trip_request_id: int
    itinerary_info: str
    traveller_details: Optional[str] = None

    class Config:
        orm_mode = True
