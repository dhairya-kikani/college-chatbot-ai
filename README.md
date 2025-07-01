### College Chatbot ###

A locally running AI-powered chatbot designed to assist college students with academic and campus-related queries. It uses a custom BERT-based model to provide intelligent responses and also logs unanswered questions for future improvement.

## Features ##

1.) BERT-based NLP for smart query understanding
2.) REST API backend using Flask
3.) Simple static frontend (HTML/CSS/JS)
4.) Logs unanswered questions to feedback.csv
5.) Admin endpoints for feedback review
6.)Built-in fallback and error handling

## Project Structure ##

```
College_Chatbot/
├── backend/
│   ├── app.py
│   ├── chatbot_engine.py
│   ├── feedback_handler.py
│   ├── logger.py
│   ├── db.py
│   ├── auth.py
│   ├── knowledge_base.json
│   ├── intent_classifier.py
│   ├── response_generator.py
│   ├── config.py
│   ├── .env
│   ├── logs/
│   │   └── server.log
│   └── data/
│       └── feedback.csv
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── admin.html
│   ├── admin.js
│
├── scripts/
│   ├── run_all.sh
│   ├── run_backend.sh
│   └── run_frontend.sh
│
├── model/
│   └── model_config.json
│
├── asset/
│   ├── Screenshot/
│   └── Video/
│
├── requirements.txt
```
## Local Setup Instructions ##

1. Clone the Repository
    ```  git clone https://github.com/dhairya-kikani/college-chatbot-ai.git ```

2. Create & Activate Environment
    Make sure you have Anaconda installed. Then run:

    ```  conda create -n tf_metal_env python=3.10 -y ```
    ```  conda activate tf_metal_env ```

3. Install Requirements
    ```  pip install -r requirements.txt ```

4. Run the Chatbot (All-in-One Script)
    ```  ./scripts/run_all.sh ```

## Tech Stack ##

- Python 3.10 – Backend
- Flask – API Framework
- HuggingFace Transformers – NLP model
- HTML/CSS/JS – Frontend
- Shell – Automation

## Developer Notes ##

- Ensure port 5000 (Flask) and 8080 (Frontend) are free.

- Script automatically handles port conflicts.

- Tokenizer warning on Mac is harmless — ignored with TOKENIZERS_PARALLELISM=false

## Contact ##
```
For queries, feature requests, or collaboration: Dhairya Kikani
Email: kikanidhairya@gmail.com
GitHub: https://github.com/dhairya-kikani
```
