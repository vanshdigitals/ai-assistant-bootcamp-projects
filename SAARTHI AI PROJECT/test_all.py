"""Test suite for SAARTHI AI core functionality."""

from utils.ai_engine import extract_intent, extract_name, extract_role
from utils.memory_manager import (
    load_user_data, save_user_data, add_goal, complete_task,
    add_journal_entry, update_goal_progress, add_milestone,
    set_user_name, set_user_role, get_active_goals, reset_user_data
)
from utils.goal_tracker import format_goals_for_display, format_stats, get_weekly_summary, get_daily_summary

passed = 0
failed = 0

def test(name, actual, expected):
    global passed, failed
    if actual == expected:
        passed += 1
    else:
        failed += 1
        print(f"  FAIL: {name} -> got '{actual}', expected '{expected}'")


print("=" * 50)
print("TESTING INTENT DETECTION")
print("=" * 50)

test("name intro", extract_intent("My name is Vansh"), "introduce")
test("goal setting", extract_intent("I want to learn Python"), "set_goal")
test("task completion", extract_intent("I completed my task"), "complete_task")
test("daily briefing", extract_intent("What should I do today?"), "daily_briefing")
test("weekly review", extract_intent("How am I doing this week?"), "weekly_review")
test("decision help", extract_intent("Should I learn React or Vue?"), "decision")
test("overwhelm", extract_intent("I am feeling overwhelmed"), "overwhelm")
test("role setting", extract_intent("I work as a developer"), "set_role")
test("general chat", extract_intent("Tell me a joke"), "general")

print("\n" + "=" * 50)
print("TESTING NAME EXTRACTION")
print("=" * 50)

test("my name is", extract_name("My name is Vansh"), "Vansh")
test("i am", extract_name("I am Priya"), "Priya")
test("i'm", extract_name("I'm Rahul"), "Rahul")
test("call me", extract_name("Call me Dev"), "Dev")
test("no name", extract_name("Hello there"), None)

print("\n" + "=" * 50)
print("TESTING ROLE EXTRACTION")
print("=" * 50)

test("work as", extract_role("I work as a software developer"), "Software Developer")
test("role is", extract_role("My role is data scientist"), "Data Scientist")
test("no role", extract_role("Hello there"), None)

print("\n" + "=" * 50)
print("TESTING MEMORY MANAGER")
print("=" * 50)

data = reset_user_data()
test("fresh data name", data['name'], "")
test("fresh data goals", data['goals'], [])

data = set_user_name(data, "TestUser")
test("set name", data['name'], "TestUser")

data = set_user_role(data, "Engineer")
test("set role", data['role'], "Engineer")

data = add_goal(data, "Learn Python")
test("add goal count", len(data['goals']), 1)
test("goal text", data['goals'][0]['text'], "Learn Python")
test("goal status", data['goals'][0]['status'], "active")

# Test duplicate prevention
data = add_goal(data, "Learn Python")
test("no duplicate", len(data['goals']), 1)

data = add_goal(data, "Build a project")
test("second goal", len(data['goals']), 2)

data = update_goal_progress(data, 0, 50)
test("progress update", data['goals'][0]['progress'], 50)

data = add_milestone(data, 0, "Complete basics")
test("milestone added", len(data['goals'][0]['milestones']), 1)

data = complete_task(data, "Finished chapter 1")
test("task completed", len(data['completed_tasks']), 1)

data = add_journal_entry(data, "Today was productive")
test("journal entry", len(data['journal']), 1)

active = get_active_goals(data)
test("active goals", len(active), 2)

print("\n" + "=" * 50)
print("TESTING GOAL TRACKER")
print("=" * 50)

stats = format_stats(data)
test("stats completed", stats['completed'], 1)
test("stats active goals", stats['active_goals'], 2)

display = format_goals_for_display(data['goals'])
test("display not empty", len(display) > 0, True)
test("display has goal", "Learn Python" in display, True)

daily = get_daily_summary(data)
test("daily has keys", 'tasks_done_today' in daily, True)

weekly = get_weekly_summary(data)
test("weekly has keys", 'tasks_done' in weekly, True)

# Clean up
reset_user_data()

print("\n" + "=" * 50)
print(f"RESULTS: {passed} passed, {failed} failed out of {passed + failed}")
print("=" * 50)

if failed == 0:
    print("\nAll tests passed!")
else:
    print(f"\n{failed} test(s) need fixing.")
