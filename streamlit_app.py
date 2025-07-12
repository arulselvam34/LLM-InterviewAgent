import streamlit as st
import json
from datetime import datetime
from interview_simulation import InterviewSimulation

st.set_page_config(page_title="LLM Interview Agent", page_icon="🤖", layout="wide")

st.title("🤖 LLM Interview Agent")
st.markdown("AI-powered interview simulation system")

# Sidebar for configuration
st.sidebar.header("Configuration")

# Job selection
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

# Model customization
st.sidebar.subheader("Customize Models")
available_models = [
    "groq/llama-3.1-8b-instant",
    "groq/llama3-8b-8192",
    "groq/gemma2-9b-it",
    "groq/mixtral-8x7b-32768",
    "groq/llama-3.1-70b-versatile"
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

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"Interview Simulation: {selected_job}")
    
    if st.button("Start Interview", type="primary"):
        # Create simulation with custom models
        simulation = InterviewSimulation(selected_job)
        simulation.models = models
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Results container
        results_container = st.container()
        
        with st.spinner("Conducting interviews..."):
            # Run interviews
            for i, candidate_id in enumerate(models.keys()):
                status_text.text(f"Interviewing {candidate_id} with {models[candidate_id]}...")
                progress_bar.progress((i + 1) / len(models))
                
                result = simulation.conduct_single_interview(candidate_id, num_questions)
                simulation.interview_results[candidate_id] = result
        
        # Display results
        st.success("Interviews completed!")
        
        # Show individual results
        for candidate_id, result in simulation.interview_results.items():
            with st.expander(f"{candidate_id}: {result['model']}", expanded=True):
                st.write(f"**Status:** {result['status'].upper()}")
                
                if result['status'] == 'completed':
                    st.write("**Interview History:**")
                    for i, qa in enumerate(result['interview_history'], 1):
                        st.write(f"**Q{i}:** {qa['question']}")
                        st.write(f"**A{i}:** {qa['answer']}")
                        st.write("---")
                    
                    st.write("**Evaluation:**")
                    st.write(result['evaluation'])
                else:
                    st.error(f"Interview failed: {result['evaluation']}")
        
        # Save results
        results = {
            "job_title": selected_job,
            "interview_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "candidates": simulation.interview_results,
            "models_used": models
        }
        
        filename = f"interview_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        st.success(f"Results saved to: {filename}")

with col2:
    st.header("Model Configuration")
    st.write("**Selected Models:**")
    for candidate, model in models.items():
        st.write(f"• {candidate}: `{model}`")
    
    st.write(f"**Questions per candidate:** {num_questions}")

# Load previous results
st.header("Previous Results")
if st.button("Load Latest Results"):
    try:
        import glob
        import os
        
        # Find latest results file
        files = glob.glob("interview_results_*.json")
        if files:
            latest_file = max(files, key=os.path.getctime)
            
            with open(latest_file, 'r') as f:
                data = json.load(f)
            
            st.subheader(f"Results from {data['interview_date']}")
            st.write(f"**Job:** {data['job_title']}")
            
            for candidate_id, result in data['candidates'].items():
                with st.expander(f"{candidate_id}: {result['model']}"):
                    st.write(f"**Status:** {result['status']}")
                    if 'interview_history' in result:
                        for i, qa in enumerate(result['interview_history'], 1):
                            st.write(f"**Q{i}:** {qa['question']}")
                            st.write(f"**A{i}:** {qa['answer']}")
                            st.write("---")
        else:
            st.info("No previous results found")
    except Exception as e:
        st.error(f"Error loading results: {e}")