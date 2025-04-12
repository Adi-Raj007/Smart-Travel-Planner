# 🏋️ Smart Travel Planner — Phase 1

Smart Travel Planner is an intelligent travel itinerary generator powered by LLMs (Large Language Models) using FastAPI and Groq's LLaMA model. It allows users to get well-structured, day-by-day trip plans based on input like destination, budget, and duration.

---

## 🚀 Features

- 📍 Generate structured day-wise travel itineraries
- 📝 Accept both form-based structured inputs and free-form prompts
- 🤖 Powered by LangChain + Groq (LLaMA3) for LLM responses
- 🌐 Interactive frontend using HTML + JavaScript
- 🔒 CORS enabled and error-handled backend

---

## 📂 Project Structure

```
Smart-Travel-Planner/
|
├── app/
│   ├── main.py                  # FastAPI backend entry point
│   ├── routes/
│   │   └── routes.py            # Pydantic models and request/response schema
│   └── template_itinerary.json  # LangChain prompt template
|
├── static/
│   ├── index.html               # Frontend HTML
│   ├── styles.css               # Styling
│   └── script.js                # JavaScript logic
|
├── .env                         # API Keys and environment vars
└── README.md                    # Project documentation
```

---

## 📌 API Endpoints

### 1. `/get_itinerary`  
Generate a structured itinerary using form-based input.

- **Method:** `POST`  
- **Request Body (JSON):**

```json
{
  "place_from": "Gaya",
  "place_to_visit": "Delhi",
  "no_of_days": 5,
  "budget": 4000
}
```

- **Response Example:**

```json
{
  "place_from": "Gaya",
  "place_to_visit": "Delhi",
  "no_of_days": 5,
  "budget": 4000,
  "days": [
    {
      "day": 1,
      "activity": "Travel from Gaya to Delhi by train...",
      "price_estimate": "₹1500"
    },
    {
      "day": 2,
      "activity": "Visit Red Fort and National Museum...",
      "price_estimate": "₹550"
    }
  ]
}
```

---

### 2. `/prompts`  
Accepts **free-form prompts** like:  
> "Plan a 4-day trip from Delhi to Gaya under ₹1200"

- **Method:** `POST`  
- **Request Body:**

```json
{
  "prompt": "Plan a 4-day trip from Delhi to Gaya under ₹1200"
}
```

- **Response:** Similar structured itinerary response as above.

---

## 🧑‍💻 How It Works

- Uses `LangChain` with `ChatGroq` (LLaMA3 70B) as backend LLM
- Structured output enforced via Pydantic models (`ItineraryRequest`, `ItineraryResponse`)
- Prompt template guides the LLM on how to format the trip output
- Two separate chains:
  - One for form-based structured input
  - Another for flexible natural-language input

---

## 🌐 Frontend UI (HTML + JS)

Frontend allows users to:
- Enter starting point, destination, number of days, and budget
- Submit the form to `/get_itinerary`
- View results day-by-day in an interactive format

📁 Files:
- `index.html`
- `styles.css`
- `script.js`

---

## 🛠️ Setup & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Travel-Planner.git
cd Smart-Travel-Planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have `python-dotenv`, `fastapi`, `uvicorn`, `langchain`, and `langchain-groq` installed.

### 3. Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

### 5. Open the Frontend

Just open `static/index.html` in your browser.

> Make sure CORS allows your frontend port (usually 5500).

---

## 🌍 Deployment Recommendations

While this is in development, for full-stack deployment later (including LLM inference), consider:
- **Render** (free FastAPI deployments)
- **Vercel / Netlify** (for frontend)
- **Replicate** or **Groq Cloud** for LLMs (paid tiers)
- **Railway / Deta / Fly.io** for backend + DB

---

## 📌 Future Enhancements (Phase 2 & 3 Ideas)

- User login & save trips
- Downloadable PDFs of itinerary
- Multilingual support
- Map integrations with Google Maps API
- Integration with hotel and flight booking APIs

---

## 🧠 Sample Prompt Ideas

- "Create a budget-friendly 3-day trip from Pune to Goa"
- "Plan a week-long solo trip to Kerala with ₹5000"
- "Family trip from Mumbai to Shimla for 4 days under ₹10,000"

---

## 👨‍💼 Author

**Your Name**  
Final Year CSE @ Central University of Haryana  
[GitHub](https://github.com/your-username) | [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📜 License

This project is licensed under the **MIT License**.

---