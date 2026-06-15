# 💪 Gym Trainer AI — Live Bootcamp Build

> Built live during the VEDAM AI Builders Bootcamp on June 14, 2026
> Mentor: Amit Kumar (Microsoft SDE) | Hosted by: VEDAM School of Technology

---

## What It Does

A personal fitness AI assistant that gives workout routines, diet plans, calorie guidance, and fitness motivation. Ask any fitness question and get instant, personalized advice powered by a local AI model running on your own machine.

---

## How It Was Built

This project was built step-by-step during a 3-hour live workshop. The notebook documents the entire learning journey:

| Step | What Was Done | Concept Learned |
|------|--------------|-----------------|
| 1 | Installed Ollama and pulled the Mistral model | Running AI models locally |
| 2 | Wrote `import ollama` and made the first API call | Python-to-AI communication |
| 3 | Asked "What is deep learning?" and got a response | Basic AI chat completion |
| 4 | Added `input()` so users can type their own questions | Dynamic user input |
| 5 | Created `ask_ai()` function to reuse the chat logic | Code modularity |
| 6 | Added a system prompt to make the AI act as a gym trainer | AI personality via system role |
| 7 | Built a Streamlit web app with text input and send button | Turning scripts into web apps |
| 8 | Added suggested questions for better user experience | UX improvement |

---

## Files

| File | Purpose |
|------|---------|
| `mybot.ipynb` | Jupyter notebook with the complete bootcamp journey. Every cell is a learning step — from first import to working chatbot. |
| `ai_assistent.py` | Final Streamlit web app. Clean UI with title, text input, suggested questions, and AI-powered responses. |

---

## Tech Stack

| Technology | Role |
|-----------|------|
| Python 3.x | Core programming language |
| Ollama | Runs AI models locally on your machine |
| Mistral 7B | Large language model used in the bootcamp |
| TinyLlama 1.1B | Lightweight alternative for low-end systems |
| Streamlit | Converts Python script into a web application |
| Jupyter Notebook | Interactive coding environment for learning |

---

## How to Run

```bash
# Install dependencies
pip install ollama streamlit jupyter

# Pull a model (pick one)
ollama pull mistral        # Better quality (needs 8GB+ RAM)
ollama pull tinyllama      # Lightweight (works on any laptop)

# For low-end systems, disable GPU
set OLLAMA_NUM_GPU=0       # Windows
export OLLAMA_NUM_GPU=0    # Mac/Linux

# Run the web app
streamlit run ai_assistent.py

# Or open the notebook
jupyter notebook mybot.ipynb
```

---

## Sample Questions to Try

| Question | What You Get |
|----------|-------------|
| Give me a 7 day diet plan to lose weight | Complete daily meal plan with Indian food options |
| What is the best workout for beginners at home? | Structured routine with sets and reps |
| How many calories should I eat to lose 5kg? | Calorie target based on general guidelines |
| Give me a morning routine for fitness | Time-blocked morning schedule |
| How to build muscle without gym equipment? | Bodyweight exercise program |

---

## Key Concepts from the Bootcamp

**System Prompt** — The hidden instruction that defines how the AI behaves. By writing "You are a gym trainer", the same AI model that answers coding questions now only talks about fitness.

**Roles in AI Chat** — Every message has a role:
- `system` — defines the AI's personality (invisible to user)
- `user` — the human's message
- `assistant` — the AI's response

**Local vs Cloud AI** — Ollama runs models on your own computer. No API key needed. No internet required. Your data stays private.

**Streamlit** — A Python library that turns any script into a web app. One command: `streamlit run app.py` and you have a working web interface.

---

## What I Learned

1. AI models can run locally on any laptop using Ollama — no cloud, no API keys, no cost
2. The system prompt is the most powerful tool in AI product design — it transforms a general model into a specialized assistant
3. Streamlit makes it possible to build and ship a web app in under 30 minutes
4. The difference between a chatbot and a product is specificity — a focused persona beats a generic assistant every time
5. Small models (TinyLlama) are fast but limited. Larger models (Mistral) give much better, more useful responses

---

## About the Bootcamp

| Detail | Info |
|--------|------|
| Event | AI Builders Bootcamp — Build Your Own ChatGPT-Style AI Assistant |
| Host | VEDAM School of Technology |
| Date | June 14-15, 2026 |
| Format | Live build-along on Zoom |
| Mentor | Amit Kumar, Software Development Engineer at Microsoft |
| Participants | 92 registered |
| Prize | Rs 10,000 Grand Prize + Mentorship for Top 5 |

---

*Built by Vansh Gupta during the VEDAM AI Builders Bootcamp*
