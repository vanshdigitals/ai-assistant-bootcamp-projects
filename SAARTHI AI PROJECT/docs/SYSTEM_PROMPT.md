# System Prompt Design — SAARTHI AI

## Philosophy

The system prompt is the most important piece of this project. A small local model (7B parameters) needs extremely clear, specific instructions to produce quality output. Vague personality descriptions lead to hallucination and generic responses.

---

## Prompt Structure

The system prompt follows a **6-section structure**:

### 1. Identity & Grounding
Establishes who Saarthi is and the cultural reference (Krishna as Arjun's charioteer). This gives the model a consistent character anchor.

### 2. Core Rules (Anti-Hallucination)
Six explicit rules that constrain the model:
- Only use ACTUAL user data
- Never invent facts
- Keep responses under 200 words
- Always end with one actionable step
- Use the user's name naturally
- Respond to goals with structure, not encouragement

### 3. Personality
Brief personality definition: warm but direct, celebrates wins, calls out procrastination. This is intentionally short — personality emerges from the rules, not adjectives.

### 4. Capabilities
Six specific capability definitions, each with explicit instructions:
- **Goal Setting** — break into monthly milestones + weekly action
- **Daily Briefing** — 3 priorities + 1 micro-win
- **Weekly Review** — accomplishments, consistency rating, next focus
- **Decision Making** — 3 clarifying questions, then recommendation
- **Overwhelm Detection** — acknowledge, pick top 3, park the rest
- **Accountability** — reference numbers, follow up on commitments

### 5. Response Format
Markdown formatting rules for consistent, readable output.

### 6. Anti-Hallucination Rules
Explicit prohibitions:
- Never reference conversations that didn't happen
- Never mention people the user hasn't mentioned
- Never cite unverified statistics or books
- Never claim the user said something they didn't
- If no goals exist, ASK — don't assume
- If no name exists, ASK — don't guess

---

## Dynamic Context Injection

At runtime, the system prompt is augmented with:

```
CURRENT USER DATA:
Name: Vansh
Role: Student
Sessions: 12
Current Streak: 5 days
Goals:
  Goal 1: Learn Python (Status: active, Progress: 40%)
    - Complete basics [DONE]
    - Build 3 projects [pending]
Recent Completed Tasks:
  - Finished Python chapter 5 (on 2026-06-14)
Recent Journal:
  [2026-06-14] Feeling more confident with functions
```

This gives the model concrete data to reference instead of inventing details.

---

## Why This Works Better Than the Original

| Original | New |
|----------|-----|
| "Be warm but direct" | Specific rules: max 200 words, end with action |
| "Track goals" | "Break into 3 monthly milestones, give ONE weekly action" |
| "Never hallucinate" | 6 explicit anti-hallucination rules |
| No user data in prompt | Full user context injected every turn |
| Vague capability list | Each capability has step-by-step instructions |
