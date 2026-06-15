# 🏹 SAARTHI AI — Personal Growth Operating System

> *"From confusion to clarity. From goals to results."*

Not just a chatbot. A mentor, strategist, and accountability partner powered by AI.

---

## The Name

**Saarthi** (सारथी) comes from the Mahabharata.

Before the great war of Kurukshetra, Arjun stood on the battlefield paralyzed by confusion, doubt, and overwhelm. He did not know what to do. He could not decide. He was frozen.

Lord Krishna did not fight for Arjun. He served as his **Saarthi** — his charioteer, guide, and trusted companion. He gave Arjun clarity when everything was unclear. Direction when every path seemed wrong. And courage when action felt impossible.

That conversation became the Bhagavad Gita.

**SAARTHI AI does the same thing.** When you are overwhelmed with goals, confused about priorities, or stuck between choices — Saarthi gives you clarity, direction, and a plan to move forward.

---

## The Problem

| Who | What They Feel |
|-----|---------------|
| Student | "I have exams, projects, internship hunting, and skill building all at once. I do not know what to do first." |
| Professional | "I feel stuck in my career but I do not know what to change or where to go next." |
| Freelancer | "I have no structure. Some days I work 14 hours, some days zero. I am all over the place." |
| Creator | "I post every day but nothing is growing. Am I doing this right?" |
| Entrepreneur | "I have 5 ideas and zero progress on any of them. I cannot decide which one to pursue." |
| Job Seeker | "I have applied to 50 jobs and heard nothing. I am losing confidence." |

**The common thread:** "I do not know if I am doing the right thing, and I have no one to ask."

---

## The Solution

SAARTHI AI is a **Personal Growth Operating System** that combines:

| Capability | What It Does |
|-----------|-------------|
| 🎯 Goal Architect | Share your goals. Saarthi breaks them into monthly milestones, weekly targets, and daily actions. |
| 📋 Daily Briefing | Every morning, get 3 priorities based on your goals. Plus one 5-minute micro-task. |
| ⚖️ Decision Engine | Stuck between two choices? Saarthi asks 3 clarifying questions, then gives a clear recommendation. |
| 🧹 Overwhelm Detector | Too many tasks? Saarthi forces you to pick the 3 that actually matter. The rest wait. |
| 📊 Accountability | Tracks what you committed to. Follows up. "You said 5 applications this week. You did 3. What blocked the other 2?" |
| 💪 Emotional Support | Validates your frustration first, then redirects to one small actionable step. |

---

## How It Works

```
You: "My name is Vansh. I want to get a design client, 
      complete my BCA semester, and build an AI portfolio."

Saarthi: "Three solid goals. Here is your 90-day roadmap:

         Goal 1 — Design Client (Week 1-4)
         Week 1: Build 3 portfolio pieces
         Week 2: Set up Behance and Instagram portfolio
         Week 3: Reach out to 10 potential clients
         Week 4: Follow up and close first project

         Goal 2 — BCA Semester (Ongoing)
         Daily: 1.5 hours focused study
         Weekly: Complete assignments 2 days before deadline

         Goal 3 — AI Portfolio (Week 5-8)
         Week 5-6: Build 2 AI projects
         Week 7: Write documentation and README
         Week 8: Push to GitHub and share on LinkedIn

         Today's action: Create your first portfolio piece.
         Open Figma. Set a 1-hour timer. Start."
```

```
You: "I have 10 things to do and I am stressed"

Saarthi: "Stop. Ten things is not a plan. It is a panic list.

You: "I finished my Figma lesson today"
Saarthi: "That is 4 days in a row. You are building a real

habit. Tomorrow: start your second portfolio project.

Same time, same energy. Keep going."

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
         Tell me all 10. I will pick the 3 that actually 
         move the needle today. The rest go to tomorrow."
```
