#!/bin/bash

set -e  # Exit if any command fails

echo "🔁 Changing to project root..."
cd "$(dirname "$0")/.."

echo "Activating virtual environment..."
source /Users/dhairyakikani/anaconda3/bin/activate tf_metal_env

echo "🛑 Checking and killing port 5000..."
if lsof -i :5000 > /dev/null; then
  kill -9 $(lsof -ti :5000)
fi

echo "🛑 Checking and killing port 8080..."
if lsof -i :8080 > /dev/null; then
  kill -9 $(lsof -ti :8080)
fi

echo "🚀 Starting Flask backend..."
cd backend
python app.py &

echo "⏳ Waiting for Flask backend to boot..."
sleep 3

echo "🚀 Starting frontend on port 8080..."
cd ../frontend
python3 -m http.server 8080 &

echo "🌐 Opening chatbot in browser..."
open http://localhost:8080

echo "✅ Everything started. Press Ctrl+C to stop."
