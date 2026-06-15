---

## Who Is It For

| Audience | How Saarthi Helps |
|----------|-------------------|
| 🎓 Students | Study plans, exam schedules, career exploration, internship hunting, skill roadmaps |
| 💼 Professionals | Career growth strategy, skill gap analysis, promotion planning, side project guidance |
| 💻 Freelancers | Client acquisition, pricing strategy, time management, portfolio building |
| 🎨 Creators | Content strategy, posting consistency, audience growth, monetization planning |
| 🚀 Entrepreneurs | Idea validation, MVP roadmap, market research, execution focus |
| 📄 Job Seekers | Resume optimization, interview prep, application tracking, networking strategy |
| 🏪 Small Business | Growth priorities, customer acquisition, operations, hiring decisions |

---

## Tech Stack

| Technology | Role |
|-----------|------|
| Python 3.x | Core programming language |
| Streamlit | Web interface — turns Python into a web app |
| Ollama | Runs AI models locally on your machine |
| Qwen2.5:3b | Default model — lightweight, works on any system |
| Mistral 7B | Optional — better quality responses, used in the bootcamp |
| Groq API | Optional — cloud-based, best response quality (free tier available) |

---

## How to Run

```bash
# Step 1: Install dependencies
pip install ollama streamlit

# Step 2: Pull a model (pick based on your system)
ollama pull qwen2.5:3b     # Works on any laptop (recommended)
ollama pull mistral         # Better quality (needs 8GB+ RAM)

# Step 3: For low-end systems, disable GPU
set OLLAMA_NUM_GPU=0        # Windows
export OLLAMA_NUM_GPU=0     # Mac/Linux

# Step 4: Run the app
cd "SAARTHI AI PROJECT"
streamlit run app.py

# Step 5: Open in browser
# http://localhost:8501
```

---

## AI Personality

Saarthi speaks like a **trusted mentor** — warm but direct, caring but no-nonsense.

| Saarthi Does | Saarthi Does Not |
|-------------|-----------------|
| Give specific, actionable advice | Give vague motivational quotes |
| Use short, clear sentences | Write long paragraphs |
| Reference your actual goals | Give generic one-size-fits-all tips |
| Celebrate your real progress | Use fake enthusiasm |
| Call out procrastination kindly | Guilt-trip or judge |
| End with one clear next action | Leave you wondering what to do |

---

## Sample Questions to Try

| Category | Question |
|----------|---------|
| Goal Setting | "I want to set my 90-day goals" |
| Daily Focus | "What should I focus on today?" |
| Overwhelm | "I am overwhelmed with too many tasks" |
| Decision | "Should I learn React or Python first?" |
| Career | "How do I get my first freelance client?" |
| Accountability | "I finished my task today — track it" |
| Motivation | "I feel like giving up" |

---

## Current Status

**MVP** — Core conversational AI is working with local models. The foundation is built. This version focuses on proving the concept: that a focused, personality-driven AI coach is more useful than a generic chatbot.

---

## Future Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| Phase 1 | Core chat with system prompt | ✅ Done |
| Phase 2 | Multiple model support (Qwen, Mistral, Groq) | ✅ Done |
| Phase 3 | Persistent memory (goals saved across sessions) | 🔜 Planned |
| Phase 4 | Goal tracking dashboard with progress charts | 🔜 Planned |
| Phase 5 | Groq API for production-quality responses | 🔜 Planned |
| Phase 6 | WhatsApp bot for daily check-ins | 📋 Future |
| Phase 7 | Mobile app (React Native) | 📋 Future |
| Phase 8 | Multi-language support (Hindi, English, Hinglish) | 📋 Future |
| Phase 9 | Team mode (accountability groups) | 📋 Future |
| Phase 10 | Public deployment as a web product | 📋 Future |

---

## The Vision

SAARTHI AI is not a weekend project. It is the starting point of a product that could help millions of people go from confusion to clarity. Every student who does not know what career to pick. Every freelancer who cannot find structure. Every entrepreneur who has ideas but no execution.

They all need a Saarthi.

---

*Built by Vansh Gupta for the VEDAM AI Builders Bootcamp competition*
*June 2026*
