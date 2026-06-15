import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), '..', 'memory', 'user_data.json')

def load_user_data():
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'name': '',
            'role': '',
            'goals': [],
            'completed_tasks': [],
            'skipped_tasks': [],
            'sessions': 0,
            'last_checkin': '',
            'streak': 0
        }

def save_user_data(data):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def update_session(data):
    data['sessions'] += 1
    data['last_checkin'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    save_user_data(data)
    return data

def add_goal(data, goal):
    data['goals'].append({
        'text': goal,
        'status': 'active',
        'created': datetime.now().strftime('%Y-%m-%d'),
        'progress': 0
    })
    save_user_data(data)
    return data

def complete_task(data, task):
    data['completed_tasks'].append({
        'task': task,
        'date': datetime.now().strftime('%Y-%m-%d')
    })
    data['streak'] += 1
    save_user_data(data)
    return data
