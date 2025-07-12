import streamlit as st
import json
from datetime import datetime
import os
import requests
import time

st.set_page_config(page_title="LLM Interview Agent", page_icon="🤖", layout="wide")

st.title("🤖 LLM Interview Agent")
st.markdown("AI-powered interview simulation system - v2.0")

# Get API key
def get_groq_api_key():
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY")

# Make API call to Groq
def call_groq_api(messages, model="llama-3.1-8b-instant", max_tokens=300):
    api_key = get_groq_api_key()
    if not api_key:
        return None
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Request failed: {str(e)}")
        return None

# Sidebar configuration
st.sidebar.header("Configuration")

job_titles = [
    "Marketing Associate",
    "Business Development Representative", 
    "Product Manager",
    "Customer Success Representative",
    "Data Analyst",
    "Content Creator",
    "AI Engineer"
]

selected_job = st.sidebar.selectbox("Select Job Position", job_titles)

available_models = [
    "llama-3.1-8b-instant",
    "llama3-8b-8192",
    "gemma2-9b-it"
]

models = {}
for i in range(1, 4):  # Reduced to 3 candidates since we only have 3 working models
    models[f"candidate{i}"] = st.sidebar.selectbox(
        f"Candidate {i} Model", 
        available_models, 
        index=i-1,
        key=f"model_{i}"
    )

num_questions = st.sidebar.slider("Number of Questions", 1, 5, 3)

# Interview functions
def generate_question(job_title, question_num, history):
    prompt = f"""You are a co-founder interviewing for a {job_title} position. 
    Generate question #{question_num} based on the interview history: {history}
    Make it relevant and professional. Return only the question."""
    
    messages = [{"role": "user", "content": prompt}]
    response = call_groq_api(messages, max_tokens=200)
    return response.strip() if response else f"Tell me about your experience relevant to {job_title}?"

def generate_answer(question, job_title, model):
    prompt = f"""You are a fresh graduate applying for {job_title}. 
    Answer this interview question professionally: {question}
    Show enthusiasm and potential despite limited experience."""
    
    messages = [{"role": "user", "content": prompt}]
    response = call_groq_api(messages, model=model, max_tokens=300)
    return response.strip() if response else "I have academic experience and strong motivation to learn."

def evaluate_candidate(job_title, history):
    prompt = f"""As a hiring manager, evaluate this {job_title} candidate based on their interview:
    {history}
    
    Provide: Decision (Pass/Fail), Score (0-100), Key Strengths, Areas for Improvement"""
    
    messages = [{"role": "user", "content": prompt}]
    response = call_groq_api(messages, max_tokens=400)
    return response.strip() if response else "Evaluation completed - candidate shows potential for growth."

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"Interview Simulation: {selected_job}")
    
    if st.button("Start Interview", type="primary"):
        if not get_groq_api_key():
            st.error("⚠️ Please configure your GROQ API key to use this application.")
            st.stop()
        results = {}
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, (candidate_id, model) in enumerate(models.items()):
            status_text.text(f"Interviewing {candidate_id} with {model}...")
            
            # Conduct interview
            history = []
            for q_num in range(1, num_questions + 1):
                question = generate_question(selected_job, q_num, history)
                time.sleep(2)  # Increase delay to avoid rate limits
                answer = generate_answer(question, selected_job, model)
                time.sleep(1)  # Add delay between API calls
                history.append({"question": question, "answer": answer})
            
            # Evaluate
            evaluation = evaluate_candidate(selected_job, history)
            
            results[candidate_id] = {
                "model": model,
                "history": history,
                "evaluation": evaluation,
                "status": "completed"
            }
            
            progress_bar.progress((i + 1) / len(models))
        
        st.success("Interviews completed!")
        
        # Display results
        for candidate_id, result in results.items():
            with st.expander(f"{candidate_id}: {result['model']}", expanded=True):
                st.write("**Interview History:**")
                for i, qa in enumerate(result['history'], 1):
                    st.write(f"**Q{i}:** {qa['question']}")
                    st.write(f"**A{i}:** {qa['answer']}")
                    st.write("---")
                
                st.write("**Evaluation:**")
                st.write(result['evaluation'])
        
        # Save results
        filename = f"interview_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump({
                "job_title": selected_job,
                "interview_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "candidates": results,
                "models_used": models
            }, f, indent=2)
        
        st.success(f"Results saved to: {filename}")

with col2:
    st.header("Model Configuration")
    st.write("**Selected Models:**")
    for candidate, model in models.items():
        st.write(f"• {candidate}: `{model}`")
    
    st.write(f"**Questions per candidate:** {num_questions}")

# Check API key availability
if not get_groq_api_key():
    st.error("⚠️ Please configure your GROQ API key to use this application.")