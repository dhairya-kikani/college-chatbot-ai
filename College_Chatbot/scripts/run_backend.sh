#!/bin/bash

echo "Activating virtual environment"
source /Users/dhairyakikani/anaconda3/bin/activate tf_metal_env

echo "Starting Flask backend..."
cd ../backend
python app.py