# Project Architecture — SAARTHI AI

## Overview

SAARTHI AI follows a clean 3-layer architecture: **UI Layer → Logic Layer → Data Layer**. Each layer has a single responsibility and communicates through well-defined function interfaces.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────┐
│                 STREAMLIT UI                 │
│                  (app.py)                    │
│                                             │
│  ┌──────────┐ ┌──────────┐ ┌────────────┐  │
│  │   Chat   │ │  Goals   │ │   Stats    │  │
│  │   View   │ │Dashboard │ │  & Journal │  │
│  └────┬─────┘ └────┬─────┘ └─────┬──────┘  │
└───────┼─────────────┼─────────────┼─────────┘
        │             │             │
┌───────▼─────────────▼─────────────▼─────────┐
│               LOGIC LAYER                    │
│                                              │
│  ┌──────────────┐  ┌──────────────────────┐  │
│  │  ai_engine   │  │   goal_tracker       │  │
│  │  - chat()    │  │   - format_goals()   │  │
│  │  - intents() │  │   - stats()          │  │
│  │  - extract() │  │   - summaries()      │  │
│  └──────┬───────┘  └──────────────────────┘  │
└─────────┼────────────────────────────────────┘
          │
┌─────────▼────────────────────────────────────┐
│               DATA LAYER                     │
│                                              │
│  ┌──────────────────┐  ┌──────────────────┐  │
│  │ memory_manager   │  │  Ollama Server   │  │
│  │ - load/save JSON │  │  - qwen2.5:7b    │  │
│  │ - CRUD goals     │  │  - local only    │  │
│  │ - CRUD tasks     │  └──────────────────┘  │
│  └──────────────────┘                        │
│                                              │
│  ┌──────────────────┐  ┌──────────────────┐  │
│  │ user_data.json   │  │ system_prompt.txt│  │
│  └──────────────────┘  └──────────────────┘  │
└──────────────────────────────────────────────┘
```

---

## Layer Details

### 1. UI Layer (`app.py`)

**Responsibility:** Render the interface, capture user input, display AI responses.

- **Chat View** — Main conversation interface with stat cards
- **Goals Dashboard** — Visual goal management with progress sliders and milestones
- **Stats View** — Daily/weekly summaries, metrics, goal progress overview
- **Journal View** — Reflection entries with history

Key pattern: The UI never calls Ollama directly. All AI communication goes through `ai_engine.py`.

### 2. Logic Layer (`utils/`)

#### `ai_engine.py`
- `chat_with_saarthi()` — Builds the prompt, manages conversation history, calls Ollama
- `extract_intent()` — Classifies user message into action categories (set_goal, complete_task, etc.)
- `extract_name()` / `extract_role()` — Regex-based NLP to pull structured data from messages
- `build_user_context()` — Formats user data into a string the model can reference
- `trim_history()` — Conversation windowing to prevent context overflow

#### `goal_tracker.py`
- `format_goals_for_display()` — Renders goals with progress bars for the sidebar
- `format_stats()` — Aggregates all metrics into a single stats dictionary
- `get_daily_summary()` / `get_weekly_summary()` — Time-scoped progress reports
- `calculate_goal_health()` — Determines if a goal is ahead, on track, or behind

### 3. Data Layer (`memory/`, `prompts/`)

#### `memory_manager.py`
- All CRUD operations for user data
- Automatic schema migration (merges new fields with existing data)
- Streak calculation with proper date handling
- Journal with automatic size limiting (50 entries max)

#### Storage
- `user_data.json` — Single source of truth for all user state
- `system_prompt.txt` — AI behavior definition, loaded at each conversation turn

---

## Data Flow: User Message Processing

```
User types message
    │
    ▼
extract_intent() → classify message type
    │
    ▼
extract_name/role() → update memory if intro detected
    │
    ▼
build_user_context() → format user data for prompt
    │
    ▼
chat_with_saarthi() → system_prompt + context + trimmed_history + message
    │
    ▼
Ollama (qwen2.5:7b) → generates response
    │
    ▼
Display response in chat UI
```

---

## Anti-Hallucination Strategy

1. **Structured system prompt** with explicit "NEVER" rules
2. **User context injection** — model always sees real user data
3. **Conversation windowing** — prevents context confusion from long histories
4. **Low temperature (0.7)** — reduces creative fabrication
5. **Repeat penalty (1.1)** — prevents repetitive/looping outputs
6. **Intent extraction before LLM** — structured data never depends on model output
