from datetime import datetime, timedelta


def format_goals_for_display(goals):
    if not goals:
        return "No goals set yet. Tell Saarthi your goals!"

    active = [g for g in goals if g.get('status') == 'active']
    completed = [g for g in goals if g.get('status') == 'completed']

    output = ""

    if active:
        for i, goal in enumerate(active, 1):
            progress = goal.get('progress', 0)
            bar = get_progress_bar(progress)
            output += f"**{i}. {goal['text']}**\n"
            output += f"{bar} {progress}%\n"

            milestones = goal.get('milestones', [])
            if milestones:
                for m in milestones:
                    icon = "✅" if m.get('done') else "⬜"
                    output += f"  {icon} {m['text']}\n"

            if goal.get('deadline'):
                output += f"  📅 Deadline: {goal['deadline']}\n"
            output += "\n"

    if completed:
        output += "**Completed:**\n"
        for goal in completed:
            output += f"  ✅ ~~{goal['text']}~~\n"

    return output


def get_progress_bar(progress, length=10):
    filled = round(progress / 100 * length)
    empty = length - filled
    return "█" * filled + "░" * empty


def format_stats(data):
    total_completed = len(data.get('completed_tasks', []))
    total_skipped = len(data.get('skipped_tasks', []))
    streak = data.get('streak', 0)
    longest_streak = data.get('longest_streak', 0)
    sessions = data.get('sessions', 0)
    active_goals = len([g for g in data.get('goals', []) if g.get('status') == 'active'])
    completed_goals = len([g for g in data.get('goals', []) if g.get('status') == 'completed'])

    total = total_completed + total_skipped
    rate = round(total_completed / max(total, 1) * 100)

    return {
        'completed': total_completed,
        'skipped': total_skipped,
        'streak': streak,
        'longest_streak': longest_streak,
        'sessions': sessions,
        'completion_rate': rate,
        'active_goals': active_goals,
        'completed_goals': completed_goals,
    }


def get_weekly_summary(data):
    week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    week_tasks = [t for t in data.get('completed_tasks', []) if t.get('date', '') >= week_ago]
    week_skipped = [t for t in data.get('skipped_tasks', []) if t.get('date', '') >= week_ago]

    active_goals = [g for g in data.get('goals', []) if g.get('status') == 'active']

    return {
        'tasks_done': len(week_tasks),
        'tasks_skipped': len(week_skipped),
        'task_list': [t['task'] for t in week_tasks],
        'active_goals': len(active_goals),
        'avg_progress': round(
            sum(g.get('progress', 0) for g in active_goals) / max(len(active_goals), 1)
        ),
    }


def get_daily_summary(data):
    today = datetime.now().strftime('%Y-%m-%d')

    today_tasks = [t for t in data.get('completed_tasks', []) if t.get('date') == today]
    active_goals = [g for g in data.get('goals', []) if g.get('status') == 'active']

    return {
        'tasks_done_today': len(today_tasks),
        'task_list': [t['task'] for t in today_tasks],
        'active_goals': len(active_goals),
        'streak': data.get('streak', 0),
    }


def calculate_goal_health(goal):
    progress = goal.get('progress', 0)
    created = goal.get('created', '')

    if not created:
        return 'unknown'

    try:
        created_date = datetime.strptime(created, '%Y-%m-%d')
        days_elapsed = (datetime.now() - created_date).days
    except ValueError:
        return 'unknown'

    if days_elapsed <= 7:
        return 'new'
    if progress >= days_elapsed * 1.1:
        return 'ahead'
    if progress >= days_elapsed * 0.7:
        return 'on_track'
    return 'behind'
