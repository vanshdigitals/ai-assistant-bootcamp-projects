# Demo Script — SAARTHI AI

## Duration: 5 minutes

Use this script to demonstrate SAARTHI AI to judges or an audience. Practice it once before the actual demo.

---

## Setup (Before Demo)

1. Make sure Ollama is running
2. Run `streamlit run app.py`
3. Clear any previous chat (click "Clear Chat" in sidebar)
4. Have the browser open at `http://localhost:8501`

---

## The Demo

### Opening (30 seconds)

> "This is SAARTHI AI — a Personal Growth Operating System that runs entirely on your local machine. No cloud APIs, no data leaving your computer. The name comes from the Mahabharata — Krishna was Arjun's Saarthi, his charioteer. This AI guides you toward your goals with clarity and accountability."

### Step 1: Introduction (45 seconds)

Type: **"My name is Vansh. I am a Computer Science student."**

> "Notice how it remembers my name and role — stored locally in JSON. The sidebar updates immediately."

### Step 2: Goal Setting (60 seconds)

Type: **"I want to learn Full Stack Web Development in 90 days"**

> "Watch how it breaks this down into monthly milestones with specific weekly actions. This isn't generic advice — it's a structured plan."

### Step 3: Goals Dashboard (45 seconds)

Click **"Goals Dashboard"** in the sidebar.

> "This is the visual dashboard. You can see progress bars, manually update progress with the slider, add milestones, and archive completed goals. Everything persists between sessions."

### Step 4: Daily Briefing (45 seconds)

Click **"Daily Briefing"** in sidebar.

> "Every day, Saarthi gives you 3 prioritized actions based on your active goals, plus one quick win you can do in 15 minutes. It references your streak and recent progress."

### Step 5: Accountability (45 seconds)

Type: **"I completed my first HTML/CSS project today!"**

> "It tracks the completion, updates the streak, and connects it back to the larger goal. The stats view shows all of this in numbers."

Click **"Progress & Stats"** to show the stats dashboard.

### Step 6: Decision Making (30 seconds)

Type: **"Should I learn React or Vue.js first?"**

> "Instead of giving a random opinion, it asks clarifying questions tied to my stated goals, then gives a recommendation with reasoning."

### Closing (30 seconds)

> "Key technical highlights: Qwen 2.5 7B model via Ollama, anti-hallucination prompt engineering, conversation windowing, intent detection, persistent memory. All running locally. Thank you."

---

## Backup Prompts (If Demo Goes Wrong)

If a response is slow or odd, use these reliable prompts:
- "What are my current goals?"
- "Give me my weekly review"
- "I am feeling overwhelmed with too many tasks"
- "Help me decide between two career options"

---

## Key Points to Emphasize

1. **100% Local** — No cloud, no API costs, complete privacy
2. **Memory** — Remembers name, goals, progress across sessions
3. **Structure** — Breaks goals into actionable milestones, not vague advice
4. **Accountability** — Tracks streaks, follows up on commitments
5. **Anti-Hallucination** — Engineered prompt design prevents fabrication
6. **Professional UI** — Multiple views: chat, goals, stats, journal
