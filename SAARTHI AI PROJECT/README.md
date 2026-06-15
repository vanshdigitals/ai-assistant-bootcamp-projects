# SAARTHI AI — Personal Growth Operating System

Not just a chatbot. A mentor, strategist, and accountability partner powered by AI.

## The Name
Saarthi comes from the Mahabharata. Lord Krishna served as Arjun's Saarthi (charioteer and guide) during the Kurukshetra war. He did not fight Arjun's battles. He gave him clarity, direction, and courage to fight his own. That is exactly what this AI does.

## The Problem
Every person — student, professional, freelancer, creator, entrepreneur — faces overwhelm. Too many goals, no clarity on priorities, no accountability system, no one to ask "am I on the right track?"

## The Solution
SAARTHI AI combines goal tracking, accountability, decision coaching, career guidance, and emotional support into one AI companion.

## Features (MVP)
- Goal-oriented conversations — share your goals, get a roadmap
- Daily briefing — 3 priorities for today
- Decision help — stuck between options? Saarthi helps you choose
- Overwhelm detector — too many tasks? Saarthi picks the top 3
- Accountability — tracks what you said you would do

## Who Is It For
- Students (study plans, career exploration, internships)
- Professionals (career growth, skill gaps, promotions)
- Freelancers (clients, pricing, time management)
- Creators (content strategy, consistency, growth)
- Entrepreneurs (idea validation, MVP planning, focus)
- Job Seekers (resume, interviews, applications)

## Tech Stack
- Python 3.x
- Streamlit
- Ollama (local AI)
- Qwen2.5:3b model (lightweight, runs on any system)
- Optional: Mistral model for better quality

## How to Run
1. pip install ollama streamlit
2. ollama pull qwen2.5:3b
3. For low-end systems: set OLLAMA_NUM_GPU=0
4. streamlit run app.py
5. Open http://localhost:8501

## Future Roadmap
- Persistent memory (remember goals across sessions)
- Goal tracking dashboard with progress charts
- Groq API integration for cloud-based high-quality responses
- WhatsApp bot for daily check-ins
- Mobile app
- Multi-language support (Hindi, English, Hinglish)

## Current Status
MVP — core conversational AI working with local models. This is the foundation. The full vision includes memory, tracking, and deployment as a public product.
