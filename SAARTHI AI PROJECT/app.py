import streamlit as st
from utils.ai_engine import chat_with_saarthi
from utils.memory_manager import load_user_data, save_user_data, update_session, add_goal, complete_task
from utils.goal_tracker import format_goals_for_display, format_stats

# Page config
st.set_page_config(
    page_title="SAARTHI AI",
    page_icon="🏹",
    layout="wide"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_data' not in st.session_state:
    st.session_state.user_data = load_user_data()
    st.session_state.user_data = update_session(st.session_state.user_data)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #888;
        margin-top: 0;
    }
    .stat-card {
        background: #1a1a2e;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #333;
    }
    .goal-card {
        background: #16213e;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #e94560;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🏹 SAARTHI AI")
    st.markdown("*Your Personal Growth Partner*")
    st.divider()
    
    # User Profile
    user_data = st.session_state.user_data
    if user_data['name']:
        st.markdown(f"### Welcome back, {user_data['name']}!")
        st.markdown(f"**Role:** {user_data['role']}")
        st.markdown(f"**Sessions:** {user_data['sessions']}")
        st.markdown(f"**Streak:** {user_data['streak']} days 🔥")
    else:
        st.markdown("### New here? Tell Saarthi your name and goals!")
    
    st.divider()
    
    # Goals Section
    st.markdown("### 🎯 Your Goals")
    st.markdown(format_goals_for_display(user_data.get('goals', [])))
    
    st.divider()
    
    # Stats
    stats = format_stats(user_data)
    st.markdown("### 📊 Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tasks Done", stats['completed'])
        st.metric("Streak", f"{stats['streak']} 🔥")
    with col2:
        st.metric("Sessions", stats['sessions'])
        st.metric("Rate", f"{stats['completion_rate']}%")
    
    st.divider()
    
    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    if st.button("📋 Daily Briefing", use_container_width=True):
        st.session_state.quick_action = "What should I focus on today? Give me my daily briefing."
    if st.button("📊 Weekly Review", use_container_width=True):
        st.session_state.quick_action = "Give me my weekly review. How am I doing on my goals?"
    if st.button("🎯 Set New Goal", use_container_width=True):
        st.session_state.quick_action = "I want to set a new goal."
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Main Chat Area
st.markdown('<p class="main-title">🏹 SAARTHI AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Personal Growth Operating System — Mentor • Strategist • Accountability Partner</p>', unsafe_allow_html=True)

st.divider()

# Display chat history
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.chat_message("user").write(message['content'])
    else:
        st.chat_message("assistant", avatar="🏹").write(message['content'])

# Welcome message if no history
if not st.session_state.chat_history:
    welcome = """Hey! I am **Saarthi** — your personal growth partner. 🏹

Think of me as your mentor, strategist, and accountability buddy — all in one.

I will remember your goals, track your progress, and hold you accountable.

**Tell me: what are the 3 biggest things you want to achieve in the next 90 days?**

Or try one of these:"""
    st.chat_message("assistant", avatar="🏹").write(welcome)
    
    st.markdown("""
> 💡 **Try asking:**
> 1. I want to set my 90-day goals
> 2. What should I focus on today?
> 3. I am feeling overwhelmed with too many tasks
> 4. Help me decide between two career options
> 5. I completed my task today — track it!
""")

# Handle quick actions
if 'quick_action' in st.session_state:
    quick = st.session_state.quick_action
    del st.session_state.quick_action
    
    st.session_state.chat_history.append({'role': 'user', 'content': quick})
    
    # Build context with user data
    context = f"\n[USER CONTEXT: Name={user_data.get('name', 'unknown')}, Role={user_data.get('role', 'unknown')}, Goals={[g['text'] for g in user_data.get('goals', [])]}, Streak={user_data.get('streak', 0)}, Sessions={user_data.get('sessions', 0)}]\n"
    
    with st.spinner("Saarthi is thinking... 🏹"):
        response = chat_with_saarthi(context + quick, st.session_state.chat_history[:-1])
    
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    st.rerun()

# Chat input
user_input = st.chat_input("Tell Saarthi about your goals, ask for advice, or check in...")

if user_input:
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})
    
    # Check if user is sharing name/profile info
    lower_input = user_input.lower()
    if 'my name is' in lower_input or 'i am' in lower_input:
        words = user_input.split()
        for i, word in enumerate(words):
            if word.lower() in ['is', 'am'] and i + 1 < len(words):
                potential_name = words[i + 1].strip('.,!').capitalize()
                if len(potential_name) > 1:
                    user_data['name'] = potential_name
                    save_user_data(user_data)
                    break
    
    # Build context
    context = f"\n[USER CONTEXT: Name={user_data.get('name', 'unknown')}, Role={user_data.get('role', 'unknown')}, Goals={[g['text'] for g in user_data.get('goals', [])]}, Streak={user_data.get('streak', 0)}, Completed Tasks={len(user_data.get('completed_tasks', []))}]\n"
    
    with st.spinner("Saarthi is thinking... 🏹"):
        response = chat_with_saarthi(context + user_input, st.session_state.chat_history[:-1])
    
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    st.rerun()
