import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from chatbot_engine import get_response
from feedback_handler import log_unanswered
from logger import log_event

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        query = data.get("query", "").strip()

        if not query:
            return jsonify({"response": "Please enter a valid question."}), 400

        response = get_response(query)

        if "Sorry" in response:
            log_unanswered(query)

        log_event("groq_fallback", {"query": query, "response": response})
        return jsonify({"response": response})

    except Exception as e:
        log_event("error", {"error": str(e)})
        return jsonify({"response": "Internal state error"}), 500

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Chatbot API running"}), 200

@app.route("/admin/feedback", methods=['GET'])
def get_feedback():
    try:
        return send_file("feedback.txt", mimetype="text/plain")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/unanswered", methods=["GET"])
def get_unanswered():
    try:
        with open("backend/data/feedback.csv", encoding="utf-8") as f:
            lines = f.readlines()
        output = []
        for line in lines:
            if "," in line:
                timestamp, query = line.strip().split(",", 1)
                output.append({"timestamp": timestamp, "query": query})
        return jsonify(output)
    except FileNotFoundError:
        return jsonify([]), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
