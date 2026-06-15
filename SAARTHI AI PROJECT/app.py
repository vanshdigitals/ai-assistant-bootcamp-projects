import streamlit as st
from datetime import datetime
from utils.ai_engine import (
    chat_with_saarthi, extract_intent, extract_name, extract_role
)
from utils.memory_manager import (
    load_user_data, save_user_data, update_session,
    set_user_name, set_user_role, add_goal, complete_task,
    add_journal_entry, get_active_goals, get_today_tasks
)
from utils.goal_tracker import (
    format_goals_for_display, format_stats,
    get_weekly_summary, get_daily_summary, get_progress_bar
)

# --- Page Config ---
st.set_page_config(
    page_title="SAARTHI AI — Personal Growth OS",
    page_icon="🏹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Session State Init ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_data' not in st.session_state:
    st.session_state.user_data = load_user_data()
    st.session_state.user_data = update_session(st.session_state.user_data)
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'chat'

user_data = st.session_state.user_data

# --- Custom CSS ---
st.markdown("""
<style>
    /* Global */
    .block-container { padding-top: 1rem; }

    /* Header */
    .hero-title {
        text-align: center;
        font-size: 2.2em;
        font-weight: 800;
        margin-bottom: 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1em;
        color: #888;
        margin-top: 0;
        margin-bottom: 1rem;
    }

    /* Stat Cards */
    .stat-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #2a2a4a;
        transition: transform 0.2s;
    }
    .stat-card:hover { transform: translateY(-2px); }
    .stat-number {
        font-size: 1.8em;
        font-weight: 800;
        color: #667eea;
    }
    .stat-label {
        font-size: 0.8em;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Goal Cards */
    .goal-card {
        background: linear-gradient(135deg, #16213e 0%, #1a1a3e 100%);
        padding: 1rem 1.2rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a1a 0%, #1a1a2e 100%);
    }
    [data-testid="stSidebar"] .stMarkdown h2 {
        color: #667eea;
    }

    /* Chat */
    .stChatMessage { border-radius: 12px; }

    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }

    /* Progress bar override */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
    }
</style>
""", unsafe_allow_html=True)


# =============================================
# SIDEBAR
# =============================================
with st.sidebar:
    st.markdown("## 🏹 SAARTHI AI")
    st.markdown("*Personal Growth Operating System*")
    st.divider()

    # --- User Profile ---
    if user_data.get('name'):
        st.markdown(f"### Welcome, {user_data['name']}! 👋")
        if user_data.get('role'):
            st.markdown(f"🎯 **{user_data['role']}**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**🔥 Streak:** {user_data.get('streak', 0)} days")
        with col2:
            st.markdown(f"**📅 Sessions:** {user_data.get('sessions', 0)}")
    else:
        st.info("👋 New here? Tell Saarthi your name and goals!")

    st.divider()

    # --- Navigation ---
    st.markdown("### 📍 Navigation")

    if st.button("💬 Chat", use_container_width=True,
                 type="primary" if st.session_state.current_view == 'chat' else "secondary"):
        st.session_state.current_view = 'chat'
        st.rerun()

    if st.button("🎯 Goals Dashboard", use_container_width=True,
                 type="primary" if st.session_state.current_view == 'goals' else "secondary"):
        st.session_state.current_view = 'goals'
        st.rerun()

    if st.button("📊 Progress & Stats", use_container_width=True,
                 type="primary" if st.session_state.current_view == 'stats' else "secondary"):
        st.session_state.current_view = 'stats'
        st.rerun()

    if st.button("📓 Journal", use_container_width=True,
                 type="primary" if st.session_state.current_view == 'journal' else "secondary"):
        st.session_state.current_view = 'journal'
        st.rerun()

    st.divider()

    # --- Quick Actions ---
    st.markdown("### ⚡ Quick Actions")

    if st.button("📋 Daily Briefing", use_container_width=True):
        st.session_state.quick_action = "Give me my daily briefing. What should I focus on today?"
        st.session_state.current_view = 'chat'
        st.rerun()

    if st.button("📊 Weekly Review", use_container_width=True):
        st.session_state.quick_action = "Give me my weekly review. How am I doing on my goals?"
        st.session_state.current_view = 'chat'
        st.rerun()

    if st.button("🎯 Set New Goal", use_container_width=True):
        st.session_state.quick_action = "I want to set a new goal."
        st.session_state.current_view = 'chat'
        st.rerun()

    if st.button("✅ Log Completed Task", use_container_width=True):
        st.session_state.quick_action = "I completed a task today!"
        st.session_state.current_view = 'chat'
        st.rerun()

    st.divider()

    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    st.caption("Built with Ollama + Streamlit")
    st.caption(f"Model: qwen2.5:7b | Local AI")


# =============================================
# HELPER: Process user message and update memory
# =============================================
def process_message(user_input):
    intent = extract_intent(user_input)

    if intent == 'introduce':
        name = extract_name(user_input)
        if name:
            st.session_state.user_data = set_user_name(st.session_state.user_data, name)

    if intent == 'set_role':
        role = extract_role(user_input)
        if role:
            st.session_state.user_data = set_user_role(st.session_state.user_data, role)

    st.session_state.chat_history.append({'role': 'user', 'content': user_input})

    with st.spinner("Saarthi is thinking... 🏹"):
        response = chat_with_saarthi(
            user_input,
            st.session_state.chat_history[:-1],
            user_data=st.session_state.user_data
        )

    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    st.rerun()


# =============================================
# VIEW: Chat
# =============================================
def render_chat_view():
    st.markdown('<p class="hero-title">🏹 SAARTHI AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Mentor • Strategist • Accountability Partner</p>', unsafe_allow_html=True)

    # Quick stats bar
    stats = format_stats(user_data)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{stats['streak']}</div>
            <div class="stat-label">🔥 Day Streak</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{stats['active_goals']}</div>
            <div class="stat-label">🎯 Active Goals</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{stats['completed']}</div>
            <div class="stat-label">✅ Tasks Done</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-number">{stats['completion_rate']}%</div>
            <div class="stat-label">📈 Success Rate</div>
        </div>""", unsafe_allow_html=True)

    st.divider()

    # Handle quick actions
    if 'quick_action' in st.session_state:
        quick = st.session_state.quick_action
        del st.session_state.quick_action
        process_message(quick)

    # Chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.chat_message("user").write(message['content'])
        else:
            st.chat_message("assistant", avatar="🏹").write(message['content'])

    # Welcome message
    if not st.session_state.chat_history:
        name = user_data.get('name', '')
        if name:
            welcome = f"""Welcome back, **{name}**! 🏹

Ready to make progress today? Here's what you can do:

- **Check in** — Tell me what you accomplished or what's on your plate
- **Set goals** — Share what you want to achieve in the next 90 days
- **Get your daily briefing** — I'll prioritize your day
- **Make a decision** — Talk through tough choices with me

**What's on your mind today?**"""
        else:
            welcome = """Hey! I'm **Saarthi** — your personal growth partner. 🏹

I'll help you set goals, track progress, and stay accountable. Think of me as a mentor who actually remembers what you said you'd do.

**To get started, tell me:**
1. Your name
2. What you do (your role/field)
3. 1-3 goals you want to achieve in the next 90 days

Let's begin — **what's your name?**"""

        st.chat_message("assistant", avatar="🏹").write(welcome)

    # Chat input
    user_input = st.chat_input("Talk to Saarthi — share goals, ask for advice, or check in...")
    if user_input:
        process_message(user_input)


# =============================================
# VIEW: Goals Dashboard
# =============================================
def render_goals_view():
    st.markdown('<p class="hero-title">🎯 Goals Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Track your progress toward what matters most</p>', unsafe_allow_html=True)

    active_goals = get_active_goals(user_data)

    if not active_goals:
        st.info("🎯 No active goals yet. Go to Chat and tell Saarthi what you want to achieve!")
        return

    for i, goal in enumerate(active_goals):
        with st.container():
            st.markdown(f"""<div class="goal-card">
                <strong>Goal {i+1}:</strong> {goal['text']}
            </div>""", unsafe_allow_html=True)

            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(goal.get('progress', 0) / 100)
            with col2:
                st.markdown(f"**{goal.get('progress', 0)}%** complete")

            milestones = goal.get('milestones', [])
            if milestones:
                st.markdown("**Milestones:**")
                for j, m in enumerate(milestones):
                    done = m.get('done', False)
                    icon = "✅" if done else "⬜"
                    st.markdown(f"{icon} {m['text']}")

            if goal.get('deadline'):
                st.caption(f"📅 Deadline: {goal['deadline']}")

            # Goal management
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                new_progress = st.slider(
                    f"Update progress",
                    0, 100,
                    goal.get('progress', 0),
                    key=f"progress_{i}"
                )
                if new_progress != goal.get('progress', 0):
                    from utils.memory_manager import update_goal_progress
                    st.session_state.user_data = update_goal_progress(
                        st.session_state.user_data, i, new_progress
                    )
                    st.rerun()

            with col_b:
                new_milestone = st.text_input(
                    "Add milestone",
                    key=f"milestone_{i}",
                    placeholder="e.g., Complete Module 1"
                )
                if new_milestone:
                    from utils.memory_manager import add_milestone
                    st.session_state.user_data = add_milestone(
                        st.session_state.user_data, i, new_milestone
                    )
                    st.rerun()

            with col_c:
                if st.button(f"🗑️ Archive Goal", key=f"archive_{i}"):
                    from utils.memory_manager import remove_goal
                    st.session_state.user_data = remove_goal(
                        st.session_state.user_data, i
                    )
                    st.rerun()

            st.divider()

    # Add goal manually
    st.markdown("### ➕ Add a New Goal")
    col1, col2 = st.columns([3, 1])
    with col1:
        new_goal_text = st.text_input("Goal", placeholder="e.g., Learn Python in 90 days", key="new_goal_input")
    with col2:
        new_goal_deadline = st.date_input("Deadline (optional)", value=None, key="new_goal_deadline")

    if st.button("🎯 Add Goal", type="primary") and new_goal_text:
        deadline = new_goal_deadline.strftime('%Y-%m-%d') if new_goal_deadline else ""
        st.session_state.user_data = add_goal(st.session_state.user_data, new_goal_text, deadline)
        st.rerun()


# =============================================
# VIEW: Progress & Stats
# =============================================
def render_stats_view():
    st.markdown('<p class="hero-title">📊 Progress & Stats</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Your growth journey in numbers</p>', unsafe_allow_html=True)

    stats = format_stats(user_data)

    # Top stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔥 Current Streak", f"{stats['streak']} days")
    with col2:
        st.metric("🏆 Longest Streak", f"{stats.get('longest_streak', 0)} days")
    with col3:
        st.metric("✅ Tasks Completed", stats['completed'])
    with col4:
        st.metric("📈 Success Rate", f"{stats['completion_rate']}%")

    st.divider()

    # Tabs for different views
    tab1, tab2 = st.tabs(["📋 Daily Summary", "📊 Weekly Summary"])

    with tab1:
        daily = get_daily_summary(user_data)
        st.markdown(f"### Today — {datetime.now().strftime('%A, %B %d')}")

        if daily['task_list']:
            st.markdown("**Tasks completed today:**")
            for task in daily['task_list']:
                st.markdown(f"  ✅ {task}")
        else:
            st.info("No tasks logged today yet. Chat with Saarthi to log your progress!")

        st.markdown(f"**Active Goals:** {daily['active_goals']}")
        st.markdown(f"**Current Streak:** {daily['streak']} days 🔥")

    with tab2:
        weekly = get_weekly_summary(user_data)
        st.markdown("### This Week's Summary")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tasks Done", weekly['tasks_done'])
        with col2:
            st.metric("Tasks Skipped", weekly['tasks_skipped'])
        with col3:
            st.metric("Avg Goal Progress", f"{weekly['avg_progress']}%")

        if weekly['task_list']:
            st.markdown("**Completed this week:**")
            for task in weekly['task_list']:
                st.markdown(f"  ✅ {task}")

    st.divider()

    # Goal progress overview
    active_goals = get_active_goals(user_data)
    if active_goals:
        st.markdown("### 🎯 Goal Progress Overview")
        for goal in active_goals:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{goal['text']}**")
                st.progress(goal.get('progress', 0) / 100)
            with col2:
                st.markdown(f"### {goal.get('progress', 0)}%")

    # Session history
    st.divider()
    st.markdown("### 📅 Account Info")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Member since:** {user_data.get('created_at', 'Unknown')}")
        st.markdown(f"**Total sessions:** {stats['sessions']}")
    with col2:
        st.markdown(f"**Last check-in:** {user_data.get('last_checkin', 'Never')}")
        st.markdown(f"**Goals completed:** {stats['completed_goals']}")


# =============================================
# VIEW: Journal
# =============================================
def render_journal_view():
    st.markdown('<p class="hero-title">📓 Journal</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Reflect on your journey and capture insights</p>', unsafe_allow_html=True)

    # New entry
    st.markdown("### ✍️ New Entry")
    entry = st.text_area(
        "What's on your mind? What did you learn today?",
        placeholder="Today I realized that...",
        height=120,
        key="journal_entry"
    )
    if st.button("📝 Save Entry", type="primary") and entry:
        st.session_state.user_data = add_journal_entry(st.session_state.user_data, entry)
        st.success("Journal entry saved! ✨")
        st.rerun()

    st.divider()

    # Past entries
    journal = user_data.get('journal', [])
    if journal:
        st.markdown("### 📖 Past Entries")
        for j in reversed(journal):
            with st.expander(f"📅 {j.get('date', 'Unknown date')}"):
                st.markdown(j.get('entry', ''))
    else:
        st.info("No journal entries yet. Start writing to track your reflections!")


# =============================================
# MAIN ROUTER
# =============================================
view = st.session_state.current_view

if view == 'chat':
    render_chat_view()
elif view == 'goals':
    render_goals_view()
elif view == 'stats':
    render_stats_view()
elif view == 'journal':
    render_journal_view()
else:
    render_chat_view()
