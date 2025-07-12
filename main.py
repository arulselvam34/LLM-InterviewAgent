# main.py
import os
import sys
from interview_simulation import InterviewSimulation
from dotenv import load_dotenv

# Fix encoding issues on Windows
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"

load_dotenv()

def main():
    job_titles = [
        "Marketing Associate",
        "Business Development Representative", 
        "Product Manager",
        "Customer Success Representative",
        "Data Analyst",
        "Content Creator",
        "AI Engineer"
    ]
    
    print("\n=== LLM Interview Simulator ===")
    print("Available job positions:")
    for i, title in enumerate(job_titles):
        print(f"{i+1}. {title}")
    
    choice = input("\nSelect job position (1-7): ")
    try:
        job_title = job_titles[int(choice)-1]
    except (ValueError, IndexError):
        print("Invalid choice. Using default: Content Creator")
        job_title = "Content Creator"
    
    num_questions = input("Number of questions per interview (default 3): ")
    try:
        num_questions = int(num_questions) if num_questions else 3
    except ValueError:
        num_questions = 3
    
    print(f"\nStarting simulation for: {job_title}")
    print(f"Questions per interview: {num_questions}")
    
    simulation = InterviewSimulation(job_title)
    
    try:
        simulation.conduct_interviews(num_questions)
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Continuing with available results...")

if __name__ == "__main__":
    main()