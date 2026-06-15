# Judge Presentation — SAARTHI AI

## One-Line Pitch

**SAARTHI AI is a local-first AI accountability partner that remembers your goals, tracks your progress, and holds you to your commitments — all running on your own machine with zero cloud dependency.**

---

## Problem Statement

Students and young professionals set goals but lack consistent accountability. Generic AI chatbots give vague advice, forget context between sessions, and hallucinate fake progress. Existing productivity tools don't understand your goals well enough to give meaningful daily guidance.

---

## Solution

SAARTHI AI acts as a personal growth operating system:

| Feature | How It Works |
|---------|-------------|
| **Goal Setting** | Breaks goals into 90-day plans with monthly milestones |
| **Daily Briefing** | AI-generated daily priorities based on your active goals |
| **Accountability** | Tracks streaks, completion rates, and follows up on commitments |
| **Decision Coaching** | Structured decision framework tied to your stated goals |
| **Privacy** | 100% local — no data leaves your machine |

---

## Technical Architecture

```
Streamlit UI ─── Python Logic ─── Ollama (Qwen 2.5 7B)
                      │
                 JSON Storage
              (memory/user_data.json)
```

### Key Technical Decisions

1. **Model Selection**: Qwen 2.5 7B — benchmarked against Mistral, Phi-3, and Gemma for instruction following and reasoning quality within 4GB VRAM constraints

2. **Anti-Hallucination Engineering**: 
   - Structured system prompt with explicit constraint rules
   - User data injected as context every turn
   - Conversation windowing (last 10 messages only)
   - Temperature tuning (0.7) with repeat penalty

3. **Intent Detection Layer**: NLP extraction happens before the LLM call — name, role, and goal extraction don't depend on model output

4. **Persistent Memory**: JSON-based storage with automatic schema migration, streak calculation, and size-limited journals

---

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | Streamlit | Rapid prototyping, Python-native, professional UI |
| AI Model | Qwen 2.5 7B | Best reasoning quality at 7B parameter scale |
| Runtime | Ollama | Local model serving, easy model switching |
| Storage | JSON files | Simple, portable, no database setup |
| Language | Python | Ecosystem, Ollama SDK, Streamlit compatibility |

---

## What Makes This Different

| Generic Chatbot | SAARTHI AI |
|----------------|------------|
| Forgets everything between sessions | Persistent memory across all sessions |
| Gives vague motivational advice | Structured plans with milestones and deadlines |
| No accountability mechanism | Streak tracking, progress metrics, follow-ups |
| Cloud-dependent, privacy concerns | 100% local, zero data transmission |
| One-size-fits-all responses | Responses grounded in YOUR specific goals |

---

## Metrics & Demo Results

- Response quality significantly improved over baseline (phi3 model)
- Zero hallucinated names or fake goals (anti-hallucination prompt)
- Persistent memory across 10+ sessions tested
- 4 distinct UI views: Chat, Goals, Stats, Journal
- Average response time: 5-15 seconds on RTX 3050

---

## Future Scope

1. Voice interface for hands-free check-ins
2. Calendar integration for deadline tracking
3. Export progress reports as PDF
4. Multi-user support
5. Mobile-responsive PWA version

---

## Built By

**Vansh Gupta**
AI Assistant Bootcamp Project
