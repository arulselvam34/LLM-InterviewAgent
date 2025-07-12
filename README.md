# 🤖 LLM Interview Agent

An AI-powered interview simulation system that evaluates how different Large Language Models (LLMs) perform as job candidates in mock interviews. This project creates a controlled environment where multiple LLM models play the role of job candidates while being interviewed by a consistent AI interviewer.

## 🎯 Project Overview

This innovative system simulates realistic job interviews using AI agents, providing insights into how different language models handle professional conversations, problem-solving, and behavioral questions.

### Key Features
- 🤖 **Multi-Model Comparison**: Test 3 different LLM models simultaneously
- 💼 **7 Job Positions**: From Marketing to AI Engineering roles
- 📊 **Comprehensive Evaluation**: Automated scoring and detailed feedback
- 🔄 **Dynamic Interviews**: Questions adapt based on candidate responses
- 📈 **Real-time Results**: Live interview progress and instant results
- 💾 **Structured Results**: JSON output for further analysis
- 🌐 **Web Interface**: Easy-to-use Streamlit dashboard
- ☁️ **Cloud Deployment**: Access from anywhere via Streamlit Cloud

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Web interface)
- **LLM Provider**: Groq (High-speed inference)
- **Language**: Python 3.8+
- **Models Used**:
  - `llama-3.1-8b-instant` (Primary)
  - `llama3-8b-8192` (Alternative)
  - `gemma2-9b-it` (Latest Gemma)
- **Deployment**: Streamlit Cloud

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com/keys))

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/arulselvam34/LLM-InterviewAgent.git
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
# Create .env file and add your GROQ_API_KEY
echo 'GROQ_API_KEY="your_api_key_here"' > .env
```

5. **Run the Streamlit app**
```bash
streamlit run streamlit_app.py
```

### Online Demo

🌐 **Try it live:** [LLM Interview Agent on Streamlit Cloud](https://llm-interviewagent.streamlit.app/)

### Usage

1. **Select job position** from 7 available roles
2. **Choose AI models** for each candidate (3 candidates available)
3. **Set number of questions** (1-5)
4. **Click "Start Interview"** and watch AI candidates get interviewed!
5. **View detailed results** with scores and evaluations

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

### Interview Results Dashboard
- **Real-time Progress**: Watch interviews happen live
- **Expandable Results**: Click to view detailed Q&A for each candidate
- **Scoring System**: 0-100 scores with Pass/Fail decisions
- **Model Comparison**: Side-by-side performance analysis

### Sample Evaluation
```
Candidate 1 (llama-3.1-8b-instant): PASS - Score 92/100
✅ Strong communication skills
✅ Relevant experience examples
✅ Professional responses

Candidate 2 (llama3-8b-8192): PASS - Score 85/100
✅ Good technical knowledge
⚠️ Could improve specificity

Candidate 3 (gemma2-9b-it): PASS - Shows potential
✅ Enthusiastic responses
✅ Quick learner attitude
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
Models are easily selectable in the Streamlit interface:
- **llama-3.1-8b-instant**: Fast and reliable
- **llama3-8b-8192**: Detailed responses
- **gemma2-9b-it**: Creative and conversational

### Available Job Positions
1. Marketing Associate
2. Business Development Representative
3. Product Manager
4. Customer Success Representative
5. Data Analyst
6. Content Creator
7. AI Engineer

### Interview Settings
- **Questions per candidate**: 1-5 (adjustable slider)
- **Real-time progress**: Live updates during interviews
- **Automatic saving**: Results saved as timestamped JSON files

## 📈 Performance Insights

### Model Characteristics
- **llama-3.1-8b-instant**: Balanced, professional responses with high scores
- **llama3-8b-8192**: Detailed, analytical answers with good structure
- **gemma2-9b-it**: Creative, conversational style with enthusiasm

### Success Factors
- **Dynamic questioning**: Each question builds on previous responses
- **Consistent evaluation**: Fair scoring across all candidates
- **Real-time feedback**: Immediate results and detailed analysis
- **Rate limiting**: Built-in delays prevent API overload

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

**"API key not found"**
- Add your GROQ_API_KEY to Streamlit secrets (for cloud)
- Or create `.env` file with your API key (for local)

**"Rate limit exceeded"**
- Wait a few minutes before running again
- Reduce number of questions
- Consider upgrading your Groq plan

**"Model decommissioned"**
- App automatically uses only supported models
- Check [Groq docs](https://console.groq.com/docs/deprecations) for updates

**Local setup issues**
- Ensure you're using `streamlit run streamlit_app.py`
- Not `python streamlit_app.py`
- Install requirements: `pip install -r requirements.txt`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI**: Powerful multi-agent framework
- **Groq**: High-speed LLM inference platform
- **Open Source Community**: Inspiration and support

## 📞 Contact

- **GitHub**: [arulselvam34](https://github.com/arulselvam34)
- **Live Demo**: [Streamlit Cloud App](https://llm-interviewagent.streamlit.app/)
- **Issues**: [Report bugs here](https://github.com/arulselvam34/LLM-InterviewAgent/issues)

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ for the AI community**

*This project demonstrates the potential of AI-powered interview systems and serves as a foundation for more advanced HR technology solutions.*"# LLM-InterviewAgent" 
"# LLM-InterviewAgent" 
