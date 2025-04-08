from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
    template="""You are a professional travel planner.

    Create a detailed travel itinerary in **structured format** for the following request:
    - Starting location: {place_from}
    - Destination: {place_to_visit}
    - Trip duration: {no_of_days} days
    - Total budget: ₹{budget}

    The output should be structured as:
    - 'place_from': (string) starting city
    - 'place_to_visit': (string) destination
    - 'no_of_days': (int) number of days
    - 'days': list of daily plans. Each day must include:
        - day: (int) day number
        - activity: (string) detailed description of what to do, where to go, with timings if possible
        - price_estimate: (string) cost in INR for the day (including travel, food, tickets, etc.)

    **Constraints and expectations**:
    - Stick to the total budget of ₹{budget}
    - Include local travel suggestions, food spots, and entry tickets
    - Add one tip or suggestion per day to enhance the experience
    - Be practical and cost-aware

    Respond only with structured JSON that matches the output schema.
            """,
    input_variables=["place_to_visit", "place_from", "no_of_days", "budget"]
)
template.save('template_itinerary.json')
