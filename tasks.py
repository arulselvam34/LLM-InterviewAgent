# tasks.py
from crewai import Task
from typing import List

def create_question_task(job_title: str, interviewer, question_number: int, interview_history: List) -> Task:
    """Creates a task for generating interview questions"""
    context = "\n".join([
        f"Q{i+1}: {interaction['question']}\nA{i+1}: {interaction['answer']}"
        for i, interaction in enumerate(interview_history)
    ]) if interview_history else "No previous responses"
    
    return Task(
        description=f"""You are conducting interview question #{question_number} for the {job_title} position.
        
        Previous conversation context:
        {context}
        
        If this is the first question, ask about their motivation and background.
        For follow-up questions, analyze the candidate's previous responses and ask relevant
        questions that dig deeper into their potential, soft skills, and cultural fit.
        
        Generate a single clear, focused question that helps evaluate the candidate.
        Return ONLY the question text, nothing else.""",
        expected_output="A clear, relevant interview question based on the context and previous responses.",
        agent=interviewer
    )

def create_answer_task(question: str, candidate) -> Task:
    """Creates a task for generating candidate responses"""
    return Task(
        description=f"""You are answering this interview question: '{question}'
        
        Provide a thoughtful, honest response that:
        - Demonstrates your enthusiasm and potential
        - Draws from your academic experiences when relevant
        - Shows your willingness to learn and grow
        - Maintains professionalism while being authentic
        
        Return ONLY your response to the question, nothing else.""",
        expected_output="A professional, thoughtful response to the interview question.",
        agent=candidate
    )

def create_evaluation_task(job_title: str, interviewer, interview_history: List) -> Task:
    """Creates a task for evaluating the candidate"""
    context = "\n".join([
        f"Q{i+1}: {interaction['question']}\nA{i+1}: {interaction['answer']}"
        for i, interaction in enumerate(interview_history)
    ])
    
    return Task(
        description=f"""Based on the full interview conversation:
        
        {context}
        
        Provide a comprehensive evaluation of the candidate for the {job_title} position.
        Include:
        1. Overall Decision (PASS/FAIL)
        2. Score (0-100)
        3. Key Strengths Demonstrated
        4. Areas for Improvement
        5. Specific Tips for Future Interviews
        6. Detailed Reasoning for the Decision
        
        Format the response clearly with headers and bullet points.""",
        expected_output="A detailed evaluation report including pass/fail decision, score, strengths, areas for improvement, and specific recommendations.",
        agent=interviewer
    )

def create_comparative_analysis_task(job_title: str, interviewer, interview_results: dict, models: dict) -> Task:
    """Creates a task for comparative analysis of all candidates"""
    return Task(
        description=f"""Write a detailed comparative analysis report for the {job_title} position interviews.
        
        You conducted {len(interview_results)} interviews with different AI models.
        
        Write a complete analysis including:
        
        === INTERVIEW SUMMARY ===
        - Total candidates interviewed
        - Interview completion status
        
        === MODEL COMPARISON ===
        - Performance differences between models
        - Response quality observations
        - Communication style variations
        
        === RECOMMENDATIONS ===
        - Best performing models
        - Suggestions for improvement
        - Future interview optimization
        
        Write the full analysis now. Do not just think about it.
        """,
        expected_output="A complete detailed comparative analysis report with specific observations and recommendations.",
        agent=interviewer
    )