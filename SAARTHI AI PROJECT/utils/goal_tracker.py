def format_goals_for_display(goals):
    if not goals:
        return "No goals set yet. Tell Saarthi your goals!"
    
    output = ""
    for i, goal in enumerate(goals, 1):
        status_emoji = "🟢" if goal['status'] == 'active' else "✅" if goal['status'] == 'completed' else "⏸️"
        output += f"{status_emoji} **Goal {i}:** {goal['text']}\n"
        output += f"   Progress: {goal['progress']}% | Since: {goal['created']}\n\n"
    return output

def format_stats(data):
    total_completed = len(data.get('completed_tasks', []))
    total_skipped = len(data.get('skipped_tasks', []))
    streak = data.get('streak', 0)
    sessions = data.get('sessions', 0)
    
    return {
        'completed': total_completed,
        'skipped': total_skipped,
        'streak': streak,
        'sessions': sessions,
        'completion_rate': round(total_completed / max(total_completed + total_skipped, 1) * 100)
    }
