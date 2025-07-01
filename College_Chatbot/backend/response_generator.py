import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def fallback_response(query):
    try:
        headers = {
            "Authorization" : f"Bearer {GROQ_API_KEY}",
            "Content-Type" : "application/json"
        }
    
        payload = {
            "model" : "llama3-8b-8192",
            "messages" :[
                {"role" : "system", "content" : "You are a helpful assistance build for college students. Answer their questions clearly and concisely."},
                {"role" : "user", "content" : query}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                                 headers=headers, json=payload)
        
        result = response.json()
        print("Groq Response:", result)
        return result["choices"][0]["message"]["content"].strip()
    
    except Exception as e:
        print("Groq fallback failed", e)
        return "Sorry, I'm unable to answer."