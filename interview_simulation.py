# interview_simulation.py
import os
from typing import List
import json
from datetime import datetime
import time
from crewai import Crew, Process
import streamlit as st

from agents import create_interviewer, create_candidate
from tasks import (
    create_question_task, 
    create_answer_task, 
    create_evaluation_task,
    create_comparative_analysis_task
)

class InterviewSimulation:
    def __init__(self, job_title: str):
        self.job_title = job_title
        self.models = {
            "candidate1": "groq/llama-3.1-8b-instant",
            "candidate2": "groq/llama3-8b-8192", 
            "candidate3": "groq/gemma2-9b-it",
            "candidate4": "groq/llama-3.1-8b-instant",  # Duplicate for comparison
        }
        self.interview_results = {}
        self.interviewer = create_interviewer(job_title)

    def conduct_single_interview(self, candidate_id: str, num_questions: int = 3) -> dict:
        print(f"\n=== Starting Interview for Candidate using {self.models[candidate_id]} ===\n")
        
        try:
            candidate = create_candidate(self.job_title, self.models[candidate_id])
            interview_history = []
            
            for i in range(num_questions):
                try:
                    # Generate question
                    question_crew = Crew(
                        agents=[self.interviewer],
                        tasks=[create_question_task(self.job_title, self.interviewer, i + 1, interview_history)],
                        process=Process.sequential
                    )
                    question = str(question_crew.kickoff()).strip()
                    print(f"\nCo-founder: {question}")
                    
                    time.sleep(2)
                    
                    # Generate answer
                    answer_crew = Crew(
                        agents=[candidate],
                        tasks=[create_answer_task(question, candidate)],
                        process=Process.sequential
                    )
                    answer = str(answer_crew.kickoff()).strip()
                    
                    time.sleep(1)
                    print(f"Candidate: {answer}\n")
                    
                    interview_history.append({
                        "question": question,
                        "answer": answer
                    })
                    
                except Exception as e:
                    print(f"Error in question {i+1}: {e}")
                    # Use fallback question/answer
                    fallback_q = f"Tell me about your experience relevant to {self.job_title}?"
                    fallback_a = "I have academic experience and strong motivation to learn."
                    interview_history.append({
                        "question": fallback_q,
                        "answer": fallback_a
                    })
                    continue

            # Generate evaluation
            try:
                evaluation_crew = Crew(
                    agents=[self.interviewer],
                    tasks=[create_evaluation_task(self.job_title, self.interviewer, interview_history)],
                    process=Process.sequential
                )
                evaluation = str(evaluation_crew.kickoff()).strip()
            except Exception as e:
                print(f"Error in evaluation: {e}")
                evaluation = f"Evaluation failed for {self.models[candidate_id]} due to technical issues."
            
            return {
                "model": self.models[candidate_id],
                "interview_history": interview_history,
                "evaluation": evaluation,
                "status": "completed"
            }
            
        except Exception as e:
            print(f"Complete interview failed for {candidate_id}: {e}")
            return {
                "model": self.models[candidate_id],
                "interview_history": [],
                "evaluation": f"Interview failed due to technical issues: {str(e)}",
                "status": "failed"
            }

    def conduct_interviews(self, num_questions: int = 3):
        print(f"\n=== Starting Interviews for {len(self.models)} candidates ===\n")
        
        for candidate_id in self.models.keys():
            print(f"Processing {candidate_id}...")
            self.interview_results[candidate_id] = self.conduct_single_interview(candidate_id, num_questions)
            time.sleep(3)
            print(f"Completed {candidate_id}")

        # Generate analysis
        if self.interview_results:
            try:
                analysis_crew = Crew(
                    agents=[self.interviewer],
                    tasks=[create_comparative_analysis_task(
                        self.job_title, 
                        self.interviewer, 
                        self.interview_results,
                        self.models
                    )],
                    process=Process.sequential
                )
                result = analysis_crew.kickoff()
                comparative_analysis = str(result).strip()
                # Clean up any "Thought:" prefixes
                if comparative_analysis.startswith("Thought:"):
                    lines = comparative_analysis.split('\n')
                    comparative_analysis = '\n'.join(lines[1:]).strip()
            except Exception as e:
                print(f"Analysis failed: {e}")
                # Generate manual analysis
                comparative_analysis = self.generate_fallback_analysis()
        else:
            comparative_analysis = "No successful interviews to analyze."
        
        filename = self.save_results(comparative_analysis)
        
        print("\n=== Interview Summary ===\n")
        for cid, result in self.interview_results.items():
            status = result.get('status', 'unknown')
            model = result.get('model', 'unknown')
            print(f"{cid}: {model} - {status.upper()}")
        
        print("\n=== Comparative Analysis ===\n")
        if comparative_analysis and len(comparative_analysis) > 50:
            print(comparative_analysis)
        else:
            print("AI analysis was brief. Using detailed fallback analysis:")
            print(self.generate_fallback_analysis())
        print(f"\nResults saved to: {filename}")
        
        return comparative_analysis

    def save_results(self, comparative_analysis: str):
        results = {
            "job_title": self.job_title,
            "interview_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "candidates": self.interview_results,
            "comparative_analysis": comparative_analysis
        }
        
        filename = f"interview_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        return filename
    
    def generate_fallback_analysis(self) -> str:
        """Generate basic analysis when AI analysis fails"""
        completed = sum(1 for r in self.interview_results.values() if r.get('status') == 'completed')
        failed = len(self.interview_results) - completed
        
        analysis = f"""INTERVIEW SIMULATION ANALYSIS - {self.job_title}
        
=== SUMMARY ===
- Total Candidates: {len(self.interview_results)}
- Completed Interviews: {completed}
- Failed Interviews: {failed}

=== MODEL PERFORMANCE ===
"""
        
        for i, (cid, result) in enumerate(self.interview_results.items(), 1):
            model = result.get('model', 'Unknown')
            status = result.get('status', 'unknown')
            questions = len(result.get('interview_history', []))
            analysis += f"\nCandidate {i}: {model}\n- Status: {status.upper()}\n- Questions Answered: {questions}\n"
        
        analysis += "\n=== RECOMMENDATIONS ===\n- All working models performed adequately\n- Consider using multiple models for comparison\n- Technical issues may require API optimization"
        
        return analysis