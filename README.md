# 🏹 AI Assistant Bootcamp Projects

Built at the **VEDAM AI Builders Bootcamp** (June 14-15, 2026) — a hands-on workshop on building ChatGPT-style AI assistants using Python, Ollama, and Streamlit.

This repository contains two AI assistant projects: one built live during the bootcamp, and one designed as an original project for the competition.

---

## Project 1: Gym Trainer AI (Live Bootcamp Build)

**Folder:** `AI_ASSISTANT_LIVE_BOOTCAMP_PROJECT/`

A personal gym and fitness AI assistant built live during the VEDAM bootcamp session. It answers questions about workouts, diet plans, calorie intake, and fitness routines.

### What It Does

- Answers fitness and diet questions
- Gives workout routines for beginners and advanced users
- Creates diet plans for weight loss or muscle gain
- Provides calorie guidance
- Motivates users to stay consistent

### Tech Stack

- Python
- Streamlit (web UI)
- Ollama (local AI model runner)
- Mistral / TinyLlama (language models)

### Files

| File | Purpose |
|------|---------|
| `mybot.ipynb` | Jupyter notebook with step-by-step bootcamp code. Covers: importing ollama, basic chat, user input, system prompts, and the gym trainer function. |
| `ai_assistent.py` | Streamlit web app for the Gym Trainer AI with text input, suggested questions, and AI responses. |

### How to Run

```bash
# Step 1: Install dependencies
pip install ollama streamlit

# Step 2: Pull a model
ollama pull mistral
# OR for low-end systems:
ollama pull tinyllama

# Step 3: Run the app
cd AI_ASSISTANT_LIVE_BOOTCAMP_PROJECT
streamlit run ai_assistent.py

# Step 4: Open browser
# Go to http://localhost:8501
```

### Sample Questions to Try

1. Give me a 7 day diet plan to lose weight
2. What is the best workout for beginners at home?
3. How many calories should I eat to lose 5kg?
4. Give me a morning routine for fitness
5. How to build muscle without gym equipment?

---

## Project 2: SAARTHI AI (Original Competition Project)

**Folder:** `SAARTHI AI PROJECT/`

SAARTHI AI is a **Personal Growth Operating System** — not just a chatbot. The name "Saarthi" comes from the Mahabharata, where Lord Krishna served as Arjun's charioteer (Saarthi), guiding him through confusion to clarity. That is exactly what this AI does.

### The Problem

Every person — student, professional, freelancer, creator, entrepreneur — faces the same core problem: **overwhelm**. Too many goals, no clarity on what to prioritize, no one to hold them accountable, and no system to track progress.

### The Solution

SAARTHI AI combines the roles of a mentor, strategist, accountability partner, and coach into one AI companion that:

- Remembers your goals
- Breaks them into daily actions
- Gives you a daily briefing of what to focus on
- Helps you make decisions when stuck
- Detects when you are overwhelmed and simplifies your task list
- Tracks what you completed and what you skipped
- Holds you accountable without guilt-tripping
- Adapts advice to your specific role and situation

### Who Is It For?

| Audience | How Saarthi Helps |
|----------|-------------------|
| Students | Study plans, exam prep, career exploration, internship hunting |
| Professionals | Career growth, skill gaps, promotion strategy |
| Freelancers | Client acquisition, pricing, time management |
| Creators | Content strategy, consistency, audience growth |
| Entrepreneurs | Idea validation, MVP planning, execution focus |
| Job Seekers | Resume, interview prep, application tracking |
| Small Business Owners | Growth strategy, priorities, customer acquisition |

### Core Features

**Goal Architect** — Share your goals. Saarthi breaks each one into monthly milestones, weekly targets, and daily actions. Creates a living roadmap.

**Daily Briefing** — Every morning, get 3 priorities for the day based on your goals. One micro-task included.

**Decision Engine** — Stuck between two choices? Saarthi asks 3 targeted questions, maps them to your goals, and gives a clear recommendation.

**Overwhelm Detector** — If you list too many tasks, Saarthi intervenes: "Stop. Pick the 3 that actually matter. The rest can wait."

**Accountability Partner** — Tracks what you committed to. Follows up. "You said 5 applications this week. You did 3. What blocked the other 2?"

**Mode Switching** — Change Saarthi's coaching style:
- Default Mentor (warm and direct)
- Drill Sergeant (tough love)
- Strategist (analytical)
- Hype Mode (pure motivation)
- Listener Mode (just validates)

### Tech Stack

- Python 3.x
- Streamlit (web interface)
- Ollama (local model runner)
- Supports multiple models:
  - `qwen2.5:1.5b` — lightweight, runs on any system
  - `mistral` — used in the live bootcamp, better quality
  - `phi3` — good balance of size and quality
- Optional: Groq API for cloud-based responses with larger models

### Project Structure

```
SAARTHI AI PROJECT/
├── saarthi.py              # Main Streamlit application
├── requirements.txt        # Python dependencies
├── prompts/
│   └── system_prompt.txt   # AI personality and behavior rules
├── utils/
│   └── ai_engine.py        # Ollama and API integration
└── .env                    # API keys (not committed)
```

### How to Run

```bash
# Step 1: Install dependencies
cd "SAARTHI AI PROJECT"
pip install ollama streamlit requests python-dotenv

# Step 2: Pull a model (pick one based on your system)
ollama pull qwen2.5:1.5b     # Light - works on any laptop
ollama pull mistral           # Medium - bootcamp model
ollama pull phi3              # Medium - good quality

# Step 3: For low-end systems, disable GPU
# On Windows:
set OLLAMA_NUM_GPU=0

# Step 4: Run the app
streamlit run saarthi.py

# Step 5: Open browser
# Go to http://localhost:8501
```

### Optional: Use Groq API for Better Responses

For much better response quality, you can use the free Groq API:

1. Sign up at [console.groq.com](https://console.groq.com)
2. Create an API key
3. Add it to the `.env` file: `GROQ_API_KEY=your_key_here`
4. Select "Cloud" mode in the app sidebar

### Sample Conversations

**Setting Goals:**
> "My name is Vansh. My 3 goals: get a graphic design client, complete BCA semester, build an AI portfolio."

**Daily Briefing:**
> "What should I focus on today?"

**Overwhelm:**
> "I have 10 things to do and I cannot handle it all"

**Decision Making:**
> "Should I learn React or Python first for my career?"

**Accountability:**
> "I finished my Figma lesson today"

---

## About the Bootcamp

**Event:** AI Builders Bootcamp — Build Your Own ChatGPT-Style AI Assistant

**Hosted by:** VEDAM School of Technology

**Date:** June 14-15, 2026

**Mentor:** Amit Kumar (Microsoft SDE)

**Format:** Live build-along workshop on Zoom

**Topics Covered:**
- Fundamentals of AI and Generative AI
- How ChatGPT and AI Assistants Work
- Prompt Engineering and AI Personalities
- AI Agents, Memory, and Context
- Building Your Own AI Chatbot
- AI Projects, Internships, and Career Opportunities

---

## What I Learned

1. **Ollama** makes it possible to run AI models locally on any laptop
2. **System prompts** define the AI's personality and behavior — this is where the real product design happens
3. **Streamlit** turns a Python script into a web app in minutes
4. **Small models** (TinyLlama, Qwen 1.5B) are fast but limited. **Medium models** (Mistral, Phi3) give much better responses. **Cloud APIs** (Groq) give the best quality.
5. The difference between a chatbot and a product is **specificity** — a focused use case with a clear persona beats a generic assistant every time

---

## Future Plans

- Add persistent memory using JSON storage so Saarthi remembers goals across sessions
- Add Groq API integration for production-quality responses
- Build a WhatsApp bot version for daily check-ins
- Add progress visualization with charts and streaks
- Deploy as a public web app

---

## Built By

**Vansh Gupta** — BCA (Cyber Security) student, graphic designer, and builder.

- GitHub: [@vanshdigitals](https://github.com/vanshdigitals)
- Brand: VanshDigitals

---

*"From confusion to clarity. From goals to results."* — SAARTHI AI
