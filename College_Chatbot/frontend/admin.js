document.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:5000/unanswered")
    .then((res) => res.json())
    .then((data) => {
        const container = document.getElementById("feedback-container");
        if (data.length === 0) {
            container.innerHTML = "<p>No unanswered queries logged.</p>";
        } else {
            data.forEach(entry => {
              const p = document.createElement("p");
              p.textContent = `${entry.timestamp} - ${entry.query}`;
              container.appendChild(p);
            });
          }
        })
        .catch(err => {
          console.error("Failed to fetch feedback log:", err);
          document.getElementById("feedback-container").innerHTML =
            "<p> Could not load data. Make sure the backend is running.</p>";
        });
    });
        
