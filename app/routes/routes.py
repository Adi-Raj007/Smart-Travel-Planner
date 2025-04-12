from pydantic import BaseModel,Field
from datetime import date,datetime
from typing import Optional


class DayPlan(BaseModel):
    day: int = Field(description="Day number in the itinerary")
    activity: str = Field(description="Description of the activity or location to visit")
    price_estimate: Optional[str] = Field(default=None, description="Estimated cost for the day or activity")

class ItineraryResponse(BaseModel):
    place_from: str
    place_to_visit: str
    no_of_days: int
    days: list[DayPlan]
    budget:int


class ItineraryRequest(BaseModel):
    place_to_visit: Optional[str] = Field(default=None,description="The Place where user want to travel or want a full itinerary")
    place_from: Optional[str] = Field(description="The place where to visit or explore")
    no_of_days: Optional[int] = Field(default=None, description="Number of Days of the itinerary")
    budget:Optional[int]=Field(default=5000,description="The total cost or budget of the trip")



class FreePromptRequest(BaseModel):
    prompt: str
