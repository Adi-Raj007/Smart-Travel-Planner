from app.routes.routes import ItineraryRequest,FreePromptRequest,ItineraryResponse,DayPlan
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
app=FastAPI()

model=ChatGroq(model="llama3-70b-8192")
structure_model=model.with_structured_output(ItineraryResponse)
template=PromptTemplate(
template="""
    Plan a concise itinerary for a traveler starting from "{place_from}" to visit "{place_to_visit}" over "{no_of_days}" days.
    Include key attractions, local experiences, and a brief recommendation for each day.
    Keep the output short, actionable, and ensure pricing details are included. And make it shorter to 1000 token and finally give itienery  in form of   table . 
    give incomplete message if data is missing.
    """,
    input_variables=["place_to_visit", "place_from", "no_of_days"]

)
free_prompt_template=PromptTemplate(
    template="""
You are a travel itinerary planner. Based on the user's input below, extract the following details:

- `place_from`: starting location
- `place_to_visit`: destination
- `no_of_days`: number of days for the trip

Then return a travel plan in **valid JSON** format that matches this schema:

ItineraryResponse {{
  place_from: str,
  place_to_visit: str,
  no_of_days: int,
  days: List[DayPlan] {{
    day: int,
    activity: str,
    price_estimate: str
  }}
}}

User input: {{prompt}}

If you can't find these three fields clearly, return:
{{ "detail": "incomplete data" }}
""",
    input_variables=["prompt"]
)
free_prompt_chain= free_prompt_template|model
chain_1= template|structure_model

@app.post(
    "/get_itinerary",
    response_model=ItineraryResponse,
    summary="Generate a structured travel itinerary",
)
async def get_itinerary(request: ItineraryRequest):
    # Invoke the LLM chain
    try:
        result = chain_1.invoke(
            {
                "place_from": request.place_from,
                "place_to_visit": request.place_to_visit,
                "no_of_days": request.no_of_days,
            }
        )
    except Exception as e:
        # You can customize error handling further here
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    # If the model returned an error detail
    if isinstance(result, dict) and result.get("detail") == "incomplete data":
        raise HTTPException(status_code=400, detail="Incomplete input data")

    return result
"""@app.post(
    "/prompts",
    summary="Free-form prompt that returns structured itinerary"
)
async def prompts(request: FreePromptRequest):
    try:
        result = free_prompt_chain.invoke({
            "user_prompt": request.prompt  # Instead, the LLM will parse this
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    if isinstance(result, dict) and result.get("detail") == "incomplete data":
        raise HTTPException(status_code=400, detail="Incomplete input data")

    return result"""
