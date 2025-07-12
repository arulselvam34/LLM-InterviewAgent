import streamlit as st
import json
from datetime import datetime
import os
from groq import Groq
import time

st.set_page_config(page_title="LLM Interview Agent", page_icon="🤖", layout="wide")

st.title("🤖 LLM Interview Agent")
st.markdown("AI-powered interview simulation system - v2.0")

# Get API key
def get_groq_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except:
        return os.getenv("GROQ_API_KEY")

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = get_groq_api_key()
    if not api_key:
        st.error("Please set GROQ_API_KEY in secrets or environment variables")
        return None
    return Groq(api_key=api_key)

client = get_groq_client()

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
    "gemma2-9b-it",
    "mixtral-8x7b-32768"
]

models = {}
for i in range(1, 5):
    models[f"candidate{i}"] = st.sidebar.selectbox(
        f"Candidate {i} Model", 
        available_models, 
        index=min(i-1, len(available_models)-1),
        key=f"model_{i}"
    )

num_questions = st.sidebar.slider("Number of Questions", 1, 5, 3)

# Interview functions
def generate_question(job_title, question_num, history):
    prompt = f"""You are a co-founder interviewing for a {job_title} position. 
    Generate question #{question_num} based on the interview history: {history}
    Make it relevant and professional. Return only the question."""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except:
        return f"Tell me about your experience relevant to {job_title}?"

def generate_answer(question, job_title, model):
    prompt = f"""You are a fresh graduate applying for {job_title}. 
    Answer this interview question professionally: {question}
    Show enthusiasm and potential despite limited experience."""
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except:
        return "I have academic experience and strong motivation to learn."

def evaluate_candidate(job_title, history):
    prompt = f"""As a hiring manager, evaluate this {job_title} candidate based on their interview:
    {history}
    
    Provide: Decision (Pass/Fail), Score (0-100), Key Strengths, Areas for Improvement"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except:
        return "Evaluation completed - candidate shows potential for growth."

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"Interview Simulation: {selected_job}")
    
    if st.button("Start Interview", type="primary") and client:
        results = {}
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, (candidate_id, model) in enumerate(models.items()):
            status_text.text(f"Interviewing {candidate_id} with {model}...")
            
            # Conduct interview
            history = []
            for q_num in range(1, num_questions + 1):
                question = generate_question(selected_job, q_num, history)
                time.sleep(1)
                answer = generate_answer(question, selected_job, model)
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

if not client:
    st.error("⚠️ Please configure your GROQ API key to use this application.")