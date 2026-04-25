# 💊 AI Medicine Info Agent

A production-style AI medicine agent that describes medicines using Gemini API and Tavily Search. It includes an LLM-as-Judge evaluation mechanism and a Streamlit UI.

## 🚀 Features

- **Medicine Description**: Provides detailed information about medicines (uses, dosage, side effects).
- **Gemini API Integration**: Uses Google's Gemini 1.5 Flash model for natural language synthesis.
- **Tavily Search Integration**: Performs real-time search for accurate medicine information.
- **LLM-as-Judge**: An automated evaluation system that rates responses based on safety, accuracy, completeness, and professionalism.
- **Streamlit UI**: A clean and interactive user interface.
- **Logging**: Keeps track of queries, responses, and evaluations.

## 📁 Project Structure

```text
ai-medicine-agent/
│
├── data/
│   └── sample_queries.txt    # Sample queries for testing
│
├── outputs/
│   └── logs.json            # JSON log of agent's activity
│
├── tools/
│   └── tavily_tool.py       # Tavily search integration
│
├── .env.example              # Example environment variables
├── .gitignore                # Files to ignore in Git
├── README.md                 # Project documentation
│
├── app.py                    # Streamlit UI
├── config.py                 # API keys & configurations
├── gemini_agents.py          # Core agent logic
├── evaluator.py              # LLM-as-Judge logic
└── requirements.txt          # Python dependencies
```

## ⚙️ Setup Instructions

### 1. Prerequisites

- Python 3.8+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- [Tavily API Key](https://tavily.com/)

### 2. Installation

1. Clone or download this project.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuration

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and replace the placeholder values with your actual API keys:
   ```text
   GEMINI_API_KEY=your_gemini_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## 🏃 Running the Project

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

Open the URL provided (usually `http://localhost:8501`) in your web browser.

## ⚖️ Evaluation

The project includes an **LLM-as-Judge** feature. Every time you analyze a medicine query, the system automatically evaluates the agent's response for:

- **Accuracy**: Is the information factually correct?
- **Safety**: Does it include necessary medical disclaimers?
- **Completeness**: Are all aspects (uses, dosage, side effects) covered?
- **Professionalism**: Is the tone appropriate for medical information?

---
**Disclaimer**: This project is for educational purposes only. Always consult with a qualified healthcare professional before taking any medication.
