import ollama
import os
import json
import re

MODEL_NAME = "qwen2.5:7b"
MAX_HISTORY_MESSAGES = 10
MAX_TOKENS = 1024

def get_system_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'system_prompt.txt')
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "You are SAARTHI AI, a personal growth operating system and accountability partner."

def build_user_context(user_data):
    goals_text = "None set yet"
    if user_data.get('goals'):
        goal_lines = []
        for i, g in enumerate(user_data['goals'], 1):
            status = g.get('status', 'active')
            progress = g.get('progress', 0)
            milestones = g.get('milestones', [])
            line = f"  Goal {i}: {g['text']} (Status: {status}, Progress: {progress}%)"
            if milestones:
                for m in milestones:
                    done = "DONE" if m.get('done') else "pending"
                    line += f"\n    - {m['text']} [{done}]"
            goal_lines.append(line)
        goals_text = "\n".join(goal_lines)

    completed_recent = []
    for t in user_data.get('completed_tasks', [])[-5:]:
        completed_recent.append(f"  - {t['task']} (on {t['date']})")
    completed_text = "\n".join(completed_recent) if completed_recent else "None yet"

    journal_recent = []
    for j in user_data.get('journal', [])[-3:]:
        journal_recent.append(f"  [{j['date']}] {j['entry'][:100]}")
    journal_text = "\n".join(journal_recent) if journal_recent else "No entries"

    return f"""CURRENT USER DATA:
Name: {user_data.get('name') or 'Not provided yet'}
Role: {user_data.get('role') or 'Not provided yet'}
Sessions: {user_data.get('sessions', 0)}
Current Streak: {user_data.get('streak', 0)} days
Goals:
{goals_text}
Recent Completed Tasks:
{completed_text}
Recent Journal:
{journal_text}"""

def trim_history(chat_history):
    if len(chat_history) <= MAX_HISTORY_MESSAGES:
        return chat_history
    return chat_history[-MAX_HISTORY_MESSAGES:]

def chat_with_saarthi(user_message, chat_history=None, user_data=None):
    system_prompt = get_system_prompt()

    if user_data:
        context = build_user_context(user_data)
        system_prompt = f"{system_prompt}\n\n{context}"

    messages = [{'role': 'system', 'content': system_prompt}]

    if chat_history:
        trimmed = trim_history(chat_history)
        for msg in trimmed:
            messages.append({
                'role': msg['role'],
                'content': msg['content']
            })

    messages.append({'role': 'user', 'content': user_message})

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            options={
                'num_predict': MAX_TOKENS,
                'temperature': 0.7,
                'top_p': 0.9,
                'repeat_penalty': 1.1,
            }
        )
        return response['message']['content']
    except ConnectionError:
        return "Could not connect to Ollama. Make sure Ollama is running (`ollama serve` in terminal)."
    except Exception as e:
        error_msg = str(e).lower()
        if "model" in error_msg and "not found" in error_msg:
            return f"Model '{MODEL_NAME}' not found. Run `ollama pull {MODEL_NAME}` in your terminal."
        return f"Something went wrong: {str(e)}"

def extract_intent(user_message):
    lower = user_message.lower().strip()

    if any(phrase in lower for phrase in ['overwhelmed', 'too much', 'stressed', "can't handle",
                                          'too many', 'burnout', 'anxious', 'feeling lost']):
        return 'overwhelm'

    if any(phrase in lower for phrase in ['i work as', 'my role is', 'i am a ', "i'm a ",
                                          'my job is']):
        return 'set_role'

    if any(phrase in lower for phrase in ['my name is', 'call me ']):
        return 'introduce'
    if any(phrase in lower for phrase in ['i am ', "i'm "]):
        name = extract_name(user_message)
        if name:
            return 'introduce'

    if any(phrase in lower for phrase in ['i want to', 'my goal', 'i plan to', 'i need to achieve',
                                          'set a goal', 'new goal', 'target is', 'aim to']):
        return 'set_goal'

    if any(phrase in lower for phrase in ['done', 'completed', 'finished', 'achieved', 'accomplished',
                                          'i did', 'task done', 'mark complete']):
        return 'complete_task'

    if any(phrase in lower for phrase in ['daily briefing', 'today', 'what should i do',
                                          'my priorities', 'focus today']):
        return 'daily_briefing'

    if any(phrase in lower for phrase in ['weekly review', 'this week', 'how am i doing',
                                          'my progress', 'weekly']):
        return 'weekly_review'

    if any(phrase in lower for phrase in ['help me decide', 'should i', 'confused between',
                                          'what do you think', 'or should i', 'decision']):
        return 'decision'

    return 'general'

def extract_name(user_message):
    lower = user_message.lower()
    patterns = [
        r"(?:my name is|i am|i'm|call me)\s+([A-Z][a-z]+)",
        r"(?:my name is|i am|i'm|call me)\s+([a-z]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, user_message, re.IGNORECASE)
        if match:
            name = match.group(1).strip().capitalize()
            if len(name) > 1 and name.lower() not in ['a', 'an', 'the', 'not', 'very', 'really', 'just', 'so']:
                return name
    return None

def extract_role(user_message):
    patterns = [
        r"(?:i work as|my role is|i am a|i'm a|my job is)\s+(?:a\s+)?(.+?)(?:\.|,|$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, user_message, re.IGNORECASE)
        if match:
            role = match.group(1).strip().rstrip('.')
            if len(role) > 2:
                return role.title()
    return None
