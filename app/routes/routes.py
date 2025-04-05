from pydantic import BaseModel,Field
from datetime import date,datetime
from typing import Optional


class DayPlan(BaseModel):
    day: int =Field(description="Days Number")
    activity: str = Field(description="Description of planned activity")
    price_estimate: Optional[str] = Field(None, description="Estimated cost")

class ItineraryResponse(BaseModel):
    place_from: str
    place_to_visit: str
    no_of_days: int
    days: list[DayPlan]


class ItineraryRequest(BaseModel):
    place_to_visit: Optional[str] = Field(default=None,description="The Place where user want to travel or want a full itinerary")
    place_from: list[str] = Field(description="The place where to visit or explore")
    no_of_days: Optional[int] = Field(default=None, description="Number of Days of the itinerary")



class FreePromptRequest(BaseModel):
    prompt: str
