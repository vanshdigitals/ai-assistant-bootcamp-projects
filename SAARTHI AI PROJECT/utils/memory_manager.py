import json
import os
from datetime import datetime, timedelta
from copy import deepcopy

MEMORY_DIR = os.path.join(os.path.dirname(__file__), '..', 'memory')
USER_DATA_FILE = os.path.join(MEMORY_DIR, 'user_data.json')

DEFAULT_USER_DATA = {
    'name': '',
    'role': '',
    'goals': [],
    'completed_tasks': [],
    'skipped_tasks': [],
    'journal': [],
    'sessions': 0,
    'last_checkin': '',
    'streak': 0,
    'longest_streak': 0,
    'created_at': '',
}

def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        merged = deepcopy(DEFAULT_USER_DATA)
        merged.update(data)
        return merged
    except (FileNotFoundError, json.JSONDecodeError):
        data = deepcopy(DEFAULT_USER_DATA)
        data['created_at'] = datetime.now().strftime('%Y-%m-%d')
        save_user_data(data)
        return data

def save_user_data(data):
    os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_session(data):
    now = datetime.now()
    today = now.strftime('%Y-%m-%d')
    last = data.get('last_checkin', '')

    data['sessions'] = data.get('sessions', 0) + 1

    if last:
        try:
            last_date = datetime.strptime(last[:10], '%Y-%m-%d').date()
            diff = (now.date() - last_date).days
            if diff == 1:
                data['streak'] = data.get('streak', 0) + 1
            elif diff > 1:
                data['streak'] = 1
        except ValueError:
            data['streak'] = 1
    else:
        data['streak'] = 1

    data['longest_streak'] = max(data.get('longest_streak', 0), data.get('streak', 0))
    data['last_checkin'] = now.strftime('%Y-%m-%d %H:%M')

    if not data.get('created_at'):
        data['created_at'] = today

    save_user_data(data)
    return data

def set_user_name(data, name):
    data['name'] = name.strip()
    save_user_data(data)
    return data

def set_user_role(data, role):
    data['role'] = role.strip()
    save_user_data(data)
    return data

def add_goal(data, goal_text, deadline=""):
    for g in data.get('goals', []):
        if g['text'].lower().strip() == goal_text.lower().strip():
            return data

    goal = {
        'text': goal_text.strip(),
        'status': 'active',
        'created': datetime.now().strftime('%Y-%m-%d'),
        'deadline': deadline,
        'progress': 0,
        'milestones': [],
    }
    data['goals'].append(goal)
    save_user_data(data)
    return data

def update_goal_progress(data, goal_index, progress):
    if 0 <= goal_index < len(data.get('goals', [])):
        data['goals'][goal_index]['progress'] = min(max(progress, 0), 100)
        if progress >= 100:
            data['goals'][goal_index]['status'] = 'completed'
        save_user_data(data)
    return data

def add_milestone(data, goal_index, milestone_text):
    if 0 <= goal_index < len(data.get('goals', [])):
        milestones = data['goals'][goal_index].get('milestones', [])
        milestones.append({
            'text': milestone_text.strip(),
            'done': False,
            'created': datetime.now().strftime('%Y-%m-%d'),
        })
        data['goals'][goal_index]['milestones'] = milestones
        save_user_data(data)
    return data

def complete_milestone(data, goal_index, milestone_index):
    goals = data.get('goals', [])
    if 0 <= goal_index < len(goals):
        milestones = goals[goal_index].get('milestones', [])
        if 0 <= milestone_index < len(milestones):
            milestones[milestone_index]['done'] = True
            done_count = sum(1 for m in milestones if m.get('done'))
            data['goals'][goal_index]['progress'] = round(done_count / len(milestones) * 100)
            save_user_data(data)
    return data

def complete_task(data, task_text):
    data['completed_tasks'].append({
        'task': task_text.strip(),
        'date': datetime.now().strftime('%Y-%m-%d'),
    })
    save_user_data(data)
    return data

def skip_task(data, task_text, reason=""):
    data['skipped_tasks'].append({
        'task': task_text.strip(),
        'reason': reason,
        'date': datetime.now().strftime('%Y-%m-%d'),
    })
    save_user_data(data)
    return data

def add_journal_entry(data, entry):
    data.setdefault('journal', []).append({
        'entry': entry.strip(),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
    })
    if len(data['journal']) > 50:
        data['journal'] = data['journal'][-50:]
    save_user_data(data)
    return data

def get_active_goals(data):
    return [g for g in data.get('goals', []) if g.get('status') == 'active']

def get_completed_goals(data):
    return [g for g in data.get('goals', []) if g.get('status') == 'completed']

def get_today_tasks(data):
    today = datetime.now().strftime('%Y-%m-%d')
    return [t for t in data.get('completed_tasks', []) if t.get('date') == today]

def get_week_tasks(data):
    week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    return [t for t in data.get('completed_tasks', []) if t.get('date', '') >= week_ago]

def remove_goal(data, goal_index):
    if 0 <= goal_index < len(data.get('goals', [])):
        data['goals'][goal_index]['status'] = 'archived'
        save_user_data(data)
    return data

def reset_user_data():
    data = deepcopy(DEFAULT_USER_DATA)
    data['created_at'] = datetime.now().strftime('%Y-%m-%d')
    save_user_data(data)
    return data
