import ollama
import streamlit as st

st.title("Your Personal Gym Trainer")

question = st.text_input("Ask anything about fitness, diet, or workout...")

st.markdown(
    """💡 Try asking:
1. Give me a 7 day diet plan to lose weight
2. What is the best workout for beginners at home?
3. How many calories should I eat to lose 5kg?
4. Give me a morning routine for fitness
5. How to build muscle without gym equipment?"""
)

def design_mentor(question):
    try:
        response = ollama.chat(
            model='tinyllama',
            messages=[
                {
                    'role': 'system',
                    'content': """You are a personal gym trainer AI assistant. rules: - Be polite and friendly - keep answers short and to the point - give diet plan for weight loss - suggest workout routines - motivate the user"""
                },
                {
                    'role': 'user',
                    'content': question
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return (
            "Error contacting the model: {}\n\nPossible actions: restart the Ollama/llama-server, "
            "ensure CUDA drivers are correctly installed or try a CPU-only model.\n\nDetails: {}".format(type(e).__name__, str(e))
        )

if st.button("Send"):
    if question:
        answer = design_mentor(question)
        st.write(answer)