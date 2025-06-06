#!/bin/bash

# Step 1: Set up virtual environment
echo "🔧 Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "📦 Installing FastAPI and Uvicorn..."
pip install --upgrade pip
pip install fastapi uvicorn

# Step 3: Launch FastAPI server
echo "🚀 Starting FastAPI backend on http://localhost:8000 ..."
uvicorn main:app --reload &

# Step 4: Open frontend
echo "🌐 Opening frontend UI..."
sleep 2  # wait for server to start
open index.html || xdg-open index.html || echo "⚠️ Please open index.html manually"

