# 🤖 LLM Interview Agent

An AI-powered interview simulation system that evaluates how different Large Language Models (LLMs) perform as job candidates in mock interviews. This project creates a controlled environment where multiple LLM models play the role of job candidates while being interviewed by a consistent AI interviewer.

## 🎯 Project Overview

This innovative system simulates realistic job interviews using AI agents, providing insights into how different language models handle professional conversations, problem-solving, and behavioral questions.

### Key Features
- 🤖 **Multi-Model Comparison**: Test 4 different LLM models simultaneously
- 💼 **7 Job Positions**: From Marketing to AI Engineering roles
- 📊 **Comprehensive Evaluation**: Automated scoring and detailed feedback
- 🔄 **Dynamic Interviews**: Questions adapt based on candidate responses
- 📈 **Comparative Analysis**: Side-by-side model performance comparison
- 💾 **Structured Results**: JSON output for further analysis

## 🛠️ Technology Stack

- **Framework**: CrewAI (Multi-agent orchestration)
- **LLM Provider**: Groq (High-speed inference)
- **Language**: Python 3.8+
- **Models Used**:
  - `groq/llama-3.1-8b-instant` (Primary)
  - `groq/llama3-8b-8192` (Alternative)
  - `groq/gemma2-9b-it` (Latest Gemma)
  - Duplicate model for comparison testing

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com/keys))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/LLM-InterviewAgent.git
cd LLM-InterviewAgent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Usage

1. **Run the simulation**
```bash
python main.py
```

2. **Select job position** (1-7)
```
1. Marketing Associate
2. Business Development Representative
3. Product Manager
4. Customer Success Representative
5. Data Analyst
6. Content Creator
7. AI Engineer
```

3. **Choose number of questions** (default: 3)

4. **Watch the AI interviews unfold!**

## 📋 Available Job Positions

| Position | Focus Areas |
|----------|-------------|
| Marketing Associate | Creativity, Communication, Campaign Strategy |
| Business Development | Sales Skills, Relationship Building, Growth Mindset |
| Product Manager | Strategic Thinking, User Focus, Technical Understanding |
| Customer Success | Problem Solving, Empathy, Customer Retention |
| Data Analyst | Analytical Skills, Technical Proficiency, Insights |
| Content Creator | Storytelling, Brand Voice, Audience Engagement |
| AI Engineer | Technical Expertise, Innovation, Problem Solving |

## 🔄 How It Works

### 1. Interview Process
```mermaid
graph LR
    A[Start] --> B[Select Job]
    B --> C[Initialize Agents]
    C --> D[Generate Questions]
    D --> E[Collect Responses]
    E --> F[Evaluate Performance]
    F --> G[Compare Models]
    G --> H[Save Results]
```

### 2. Agent Architecture
- **Interviewer Agent**: Co-founder/CEO role with consistent evaluation criteria
- **Candidate Agents**: Fresh graduates with different LLM personalities
- **Dynamic Questioning**: Follow-up questions based on previous responses

### 3. Evaluation Metrics
- **Decision**: Pass/Fail recommendation
- **Score**: 0-100 numerical rating
- **Strengths**: Key positive attributes identified
- **Improvements**: Areas for development
- **Tips**: Specific interview improvement suggestions
- **Reasoning**: Detailed evaluation logic

## 📊 Sample Output

### Interview Summary
```
candidate1: groq/llama-3.1-8b-instant - COMPLETED
candidate2: groq/llama3-8b-8192 - COMPLETED
candidate3: groq/gemma2-9b-it - COMPLETED
candidate4: groq/llama-3.1-8b-instant - COMPLETED
```

### Results Structure
```json
{
  "job_title": "AI Engineer",
  "interview_date": "2024-12-15 14:30:22",
  "candidates": {
    "candidate1": {
      "model": "groq/llama-3.1-8b-instant",
      "score": 85,
      "evaluation": "Strong technical knowledge...",
      "interview_history": [...]
    }
  },
  "comparative_analysis": "Detailed comparison..."
}
```

## 🎯 Use Cases

### For Developers
- **Model Evaluation**: Compare LLM performance in conversational scenarios
- **Prompt Engineering**: Test different personality prompts
- **Benchmarking**: Establish baseline performance metrics

### For HR Professionals
- **Interview Training**: Understand effective questioning techniques
- **Bias Analysis**: Identify potential biases in evaluation criteria
- **Process Optimization**: Improve interview structure and flow

### For Researchers
- **AI Behavior Study**: Analyze how different models handle professional scenarios
- **Conversation Analysis**: Study dialogue patterns and response quality
- **Performance Metrics**: Quantify conversational AI capabilities

## 🔧 Configuration

### Customizing Models
Edit `interview_simulation.py`:
```python
self.models = {
    "candidate1": "your-preferred-model",
    "candidate2": "another-model",
    # Add more models
}
```

### Adding Job Positions
Modify `main.py`:
```python
job_titles = [
    "Your Custom Position",
    # Add more positions
]
```

### Adjusting Questions
Update `tasks.py` to modify question generation logic.

## 📈 Performance Insights

Based on testing, here's what we've observed:

### Model Characteristics
- **Llama-3.1-8b**: Balanced, professional responses
- **Llama3-8b-8192**: More detailed, technical answers
- **Gemma2-9b**: Creative, conversational style

### Success Factors
- Clear, specific questions get better responses
- Follow-up questions reveal deeper insights
- Consistent evaluation criteria ensure fair comparison

## 🤝 Contributing

We welcome contributions! Areas for improvement:

- 📝 **New Job Positions**: Add specialized roles
- 🤖 **Additional Models**: Integrate other LLM providers
- 📊 **Enhanced Metrics**: Develop new evaluation criteria
- 🎨 **UI/UX**: Create web interface
- 📱 **Mobile Support**: Responsive design

### Development Setup
1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit pull request with detailed description

## 🐛 Troubleshooting

### Common Issues

**"Unknown error occurred"**
- Check your GROQ_API_KEY in .env file
- Verify internet connection
- Try reducing number of questions

**Models not responding**
- Some models may have rate limits
- Wait a few minutes and retry
- Check Groq service status

**Encoding errors on Windows**
- The system automatically handles Windows encoding
- Ensure Python 3.8+ is installed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI**: Powerful multi-agent framework
- **Groq**: High-speed LLM inference platform
- **Open Source Community**: Inspiration and support

## 📞 Contact

- **GitHub**: [Your GitHub Profile]
- **LinkedIn**: [Your LinkedIn Profile]
- **Email**: [Your Email]

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ for the AI community**

*This project demonstrates the potential of AI-powered interview systems and serves as a foundation for more advanced HR technology solutions.*"# LLM-InterviewAgent" 
"# LLM-InterviewAgent" 
