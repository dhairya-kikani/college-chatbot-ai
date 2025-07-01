const BASE_URL = "http://127.0.0.1:5000";

function appendMessage(sender, message) {
    const chatWindow = document.getElementById("chat-window");
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}`;
    msgDiv.innerHTML = message;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function showTyping() {
    const chatWindow = document.getElementById("chat-window");
    const typingDiv = document.createElement("div");
    typingDiv.className = "typing";
    typingDiv.id = "typing";
    typingDiv.innerHTML = "Bot is thinking...";
    chatWindow.appendChild(typingDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeTyping() {
    const typingDiv = document.getElementById("typing");
    if (typingDiv) typingDiv.remove();
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const text = input.value.trim();
    if (!text) return;

    appendMessage("user", text);
    input.value = "";

    showTyping();

    fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: text }),
    })
    .then((res) => res.json())
    .then((data) => {
        removeTyping();
        appendMessage("bot", data.response);
    })
    .catch((err) => {
        removeTyping();
        appendMessage("bot", "Error: Could not reach server.");
        console.error(err);
    });
}
