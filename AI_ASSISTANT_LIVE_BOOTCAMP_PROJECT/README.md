# Gym Trainer AI — Live Bootcamp Build

Built live during the VEDAM AI Builders Bootcamp on June 14, 2026.

## What It Does
A personal fitness AI assistant that answers questions about workouts, diet plans, calorie intake, and fitness routines.

## Files
- mybot.ipynb — Step-by-step Jupyter notebook from the bootcamp covering: importing ollama, basic AI chat, user input handling, system prompts, and building the gym trainer function
- ai_assistent.py — Streamlit web app with text input, suggested questions, and AI-powered fitness responses

## Tech Stack
Python, Streamlit, Ollama, Mistral/TinyLlama

## How to Run
1. pip install ollama streamlit
2. ollama pull mistral (or ollama pull tinyllama for low-end systems)
3. streamlit run ai_assistent.py
4. Open http://localhost:8501

## Sample Questions
1. Give me a 7 day diet plan to lose weight
2. What is the best workout for beginners at home?
3. How many calories should I eat to lose 5kg?
4. Give me a morning routine for fitness
5. How to build muscle without gym equipment?

## What I Learned
- How Ollama runs AI models locally
- System prompts define AI personality and behavior
- Streamlit converts Python scripts into web apps
- The difference between user role and system role in AI chat
