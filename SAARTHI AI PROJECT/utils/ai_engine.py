import ollama
import os

def get_system_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'system_prompt.txt')
    try:
        with open(prompt_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "You are SAARTHI AI, a personal growth operating system and accountability partner."

def chat_with_saarthi(user_message, chat_history=None):
    system_prompt = get_system_prompt()
    
    messages = [{'role': 'system', 'content': system_prompt}]
    
    if chat_history:
        for msg in chat_history:
            messages.append(msg)
    
    messages.append({'role': 'user', 'content': user_message})
    
    try:
        response = ollama.chat(
            model='tinyllama',
            messages=messages
        )
        return response['message']['content']
    except Exception as e:
        return f"Saarthi is having trouble connecting. Error: {str(e)}"
