from app.routes.routes import ItineraryRequest,FreePromptRequest,ItineraryResponse,DayPlan
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.runnables import RunnableLambda

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles







load_dotenv()
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/frontend", StaticFiles(directory="static", html=True), name="frontend")




model=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
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
        print(result)
    except Exception as e:
        # You can customize error handling further here
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    # If the model returned an error detail
    if isinstance(result, dict) and result.get("detail") == "incomplete data":
        raise HTTPException(status_code=400, detail="Incomplete input data")

    return result

# structure_data=structure_model.invoke(I)

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
        print(structured_input)
        result = chain.invoke(structured_input.model_dump())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    return result
