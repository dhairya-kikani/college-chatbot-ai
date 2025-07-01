import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util
from response_generator import fallback_response

model = SentenceTransformer('all-MiniLM-L6-v2')

kb_path = os.path.join(os.path.dirname(__file__),"knowledge_base.json")
try:
    with open(kb_path, encoding="utf-8") as f:
        kb = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    kb = {}

questions = list(kb.keys())
answers = list(kb.values())

question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_response(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarity_scores  = util.cos_sim(query_embedding, question_embeddings)[0]  # type: ignore
    best_score = similarity_scores.max().item()
    best_index = similarity_scores.argmax().item()

    if best_score > 0.6:
        return answers[best_index] # type: ignore
    return fallback_response(query)
