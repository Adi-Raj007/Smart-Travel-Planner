from app.routes.routes import ItineraryRequest,FreePromptRequest,ItineraryResponse,DayPlan
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.runnables import RunnableLambda


load_dotenv()
app=FastAPI()

model=ChatGroq(model="llama3-70b-8192")
structure_model=model.with_structured_output(ItineraryResponse)
template=load_prompt('app/template_itinerary.json')

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
                "budget":request.budget
            }
        )
    except Exception as e:
        # You can customize error handling further here
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    # If the model returned an error detail
    if isinstance(result, dict) and result.get("detail") == "incomplete data":
        raise HTTPException(status_code=400, detail="Incomplete input data")

    return result



chain = (
    RunnableLambda(lambda x: template.format(**x)) |
    model.with_structured_output(ItineraryResponse)
)

@app.post(
    "/prompts",
    response_model=ItineraryResponse,
    summary="Free-form prompt that returns structured itinerary"
)
async def prompts(request: FreePromptRequest):
    try:
        structured_input = model.with_structured_output(ItineraryRequest).invoke(request.prompt)
        result = chain.invoke(structured_input.model_dump())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    return result
