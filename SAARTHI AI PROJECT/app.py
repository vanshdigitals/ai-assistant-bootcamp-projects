import streamlit as st
import ollama

st.set_page_config(page_title="SAARTHI AI", page_icon="🏹")
st.title("🏹 SAARTHI AI")
st.caption("Your Personal Growth Partner")

SYSTEM = "You are SAARTHI AI, a personal growth coach. Be warm, direct, give specific advice. Max 150 words. End with one action step."

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    st.chat_message(m["role"]).write(m["content"])

if prompt := st.chat_input("Ask Saarthi anything..."):
    st.session_state.msgs.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("🏹 Thinking..."):
        r = ollama.chat(model="qwen2.5:3b", messages=[{"role":"system","content":SYSTEM}]+st.session_state.msgs, options={"num_predict":300})
        reply = r["message"]["content"]
    st.session_state.msgs.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
