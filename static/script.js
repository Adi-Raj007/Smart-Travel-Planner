const baseURL = "http://127.0.0.1:8000"; // Update if needed

// Handle tab switching between Structured and Free Prompt
document.querySelectorAll(".tab-button").forEach(button => {
  button.addEventListener("click", () => {
    // Remove active state from all buttons and sections
    document.querySelectorAll(".tab-button").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".form-section").forEach(section => section.classList.remove("active-section"));

    // Add active state to clicked button & corresponding section
    button.classList.add("active");
    document.getElementById(button.getAttribute("data-tab")).classList.add("active-section");
  });
});

// Structured Itinerary Form Submission
document.getElementById("itineraryForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const from = document.getElementById("from").value;
  const to = document.getElementById("to").value;
  const days = document.getElementById("days").value;
  const budget = document.getElementById("budget").value;

  document.getElementById("itineraryDisplay").innerHTML = "<p>Loading itinerary...</p>";

  try {
    const res = await fetch(`${baseURL}/get_itinerary`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        place_from: from,
        place_to_visit: to,
        no_of_days: Number(days),
        budget: Number(budget)
      })
    });

    if (!res.ok) {
      const errorResp = await res.json();
      throw new Error(errorResp.detail || "Unknown error occurred");
    }

    const data = await res.json();
    renderItinerary(data);
  } catch (err) {
    document.getElementById("itineraryDisplay").innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
  }
});

// Free Prompt Form Submission
document.getElementById("promptForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const promptText = document.getElementById("prompt").value;
  document.getElementById("itineraryDisplay").innerHTML = "<p>Loading itinerary...</p>";

  try {
    const res = await fetch(`${baseURL}/prompts`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: promptText })
    });

    if (!res.ok) {
      const errorResp = await res.json();
      throw new Error(errorResp.detail || "Unknown error occurred");
    }

    const data = await res.json();
    renderItinerary(data);
  } catch (err) {
    document.getElementById("itineraryDisplay").innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
  }
});

// Render the itinerary into interactive cards
function renderItinerary(data) {
  const itineraryDiv = document.getElementById("itineraryDisplay");
  let htmlContent = `
    <div class="summary">
      <p><strong>From:</strong> ${data.place_from}</p>
      <p><strong>To Visit:</strong> ${data.place_to_visit}</p>
      <p><strong>Duration:</strong> ${data.no_of_days} day(s)</p>
      <p><strong>Budget:</strong> ₹${data.budget}</p>
    </div>
  `;

  data.days.forEach(day => {
    htmlContent += `
      <div class="card" onclick="toggleCard(this)">
        <div class="card-header">
          <span>Day ${day.day}</span>
          <span>▼</span>
        </div>
        <div class="card-content">
          <p>${day.activity}</p>
          <p><strong>Estimated Cost:</strong> ${day.price_estimate}</p>
        </div>
      </div>
    `;
  });

  itineraryDiv.innerHTML = htmlContent;
}

// Toggle itinerary card details when clicked
function toggleCard(cardElement) {
  const contentDiv = cardElement.querySelector(".card-content");
  const arrowSpan = cardElement.querySelector(".card-header span:last-child");
  if (contentDiv.style.display === "block") {
    contentDiv.style.display = "none";
    arrowSpan.textContent = "▼";
  } else {
    contentDiv.style.display = "block";
    arrowSpan.textContent = "▲";
  }
}
