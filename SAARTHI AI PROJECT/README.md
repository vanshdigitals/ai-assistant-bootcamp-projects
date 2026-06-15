# 🏹 SAARTHI AI — Personal Growth Operating System

> *Like Krishna was Arjun's Saarthi (charioteer), this AI guides you toward your goals — with clarity, direction, and accountability.*

**SAARTHI AI** is an AI-powered personal growth assistant that runs entirely on your local machine. No cloud APIs. No data leaving your computer. Just you and a smart mentor who remembers your goals and holds you accountable.

---

## What It Does

- **Goal Setting** — Break big goals into 90-day plans with monthly milestones
- **Daily Briefing** — Get prioritized daily action items based on your active goals
- **Weekly Review** — Track what you accomplished and where to focus next
- **Progress Tracking** — Visual dashboards with streak tracking and completion rates
- **Decision Coaching** — Work through tough decisions with structured guidance
- **Accountability** — The AI remembers what you committed to and follows up
- **Journal** — Capture reflections and insights over time

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **AI Model** | Qwen 2.5 7B (via Ollama) |
| **Backend** | Python |
| **Data** | Local JSON persistence |
| **Runtime** | 100% local — no cloud APIs |

---

## Quick Start

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/vanshdigitals/ai-assistant-bootcamp-projects.git
cd "ai-assistant-bootcamp-projects/SAARTHI AI PROJECT"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull the AI model
ollama pull qwen2.5:7b

# 4. Run the app
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## Project Structure

```
SAARTHI AI PROJECT/
├── app.py                  # Streamlit UI — main application
├── requirements.txt        # Python dependencies
├── prompts/
│   └── system_prompt.txt   # AI personality and behavior rules
├── utils/
│   ├── ai_engine.py        # Ollama integration, intent detection, NLP
│   ├── memory_manager.py   # User data persistence, goal/task CRUD
│   └── goal_tracker.py     # Progress formatting, stats, summaries
├── memory/
│   └── user_data.json      # User profile and goal data (auto-created)
└── docs/
    ├── PROJECT_ARCHITECTURE.md
    ├── SYSTEM_PROMPT.md
    ├── SETUP_GUIDE.md
    ├── DEMO_SCRIPT.md
    └── JUDGE_PRESENTATION.md
```

---

## Key Design Decisions

1. **Qwen 2.5 7B** chosen for best reasoning quality within 4GB VRAM constraints
2. **Anti-hallucination prompt design** — explicit rules prevent the model from inventing facts
3. **Conversation windowing** — only last 10 messages sent to model to prevent context overflow
4. **Intent detection** — NLP layer extracts user actions (goals, tasks, name) before sending to LLM
5. **Structured system prompt** — detailed capability definitions replace vague personality descriptions

---

## Model Comparison

| Model | Reasoning | Instruction Following | VRAM | Verdict |
|-------|-----------|----------------------|------|---------|
| Qwen 2.5 7B | Excellent | Excellent | ~4.7GB | **Selected** |
| Mistral 7B | Good | Good | ~4.4GB | Good alternative |
| Phi-3 3.8B | Fair | Fair | ~2.2GB | Too small for quality |
| Gemma 2 9B | Excellent | Good | ~5.4GB | Too large for 4GB VRAM |

---

## Privacy

All data stays on your machine. The AI model runs locally through Ollama. No API calls. No telemetry. Your goals and conversations are stored in `memory/user_data.json` — a plain JSON file you can read, edit, or delete anytime.

---

## Built By

**Vansh Gupta** — AI Assistant Bootcamp Project

---

## License

MIT
