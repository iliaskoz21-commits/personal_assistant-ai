# 🤖 Multi-Agent Personal AI Assistant
> **State-of-the-art AI Orchestration using LangGraph, Local LLMs (Mistral), and Real-time RAG.**

---

### 🛠️ Tech Stack & Specialized Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/LangChain-121011?style=for-the-badge&logo=chainlink&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-6.0-FF5200?style=for-the-badge&logo=gradio&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🌟 Overview
This project showcases a **Stateful Multi-Agent Architecture** designed to act as a comprehensive personal assistant. Unlike simple chatbots, this system uses a **State Machine** to route queries to specialized agents, each equipped with real-time internet access via the **Tavily Search API**.

<img width="1872" height="847" alt="multi agent personal assistant prinscreen" src="https://github.com/user-attachments/assets/7cf4df28-43a4-49b6-8a7a-3a84646ef314" />



## 🏗️ System Architecture
The application is built on three core pillars:
1. **The Brain (Ollama/Mistral):** High-performance local inference ensuring data privacy and reduced latency.
2. **The Orchestrator (LangGraph):** Manages the flow between nodes (Weather, News, Health, Culture) and maintains a persistent state.
3. **The Memory (SQLite):** A robust checkpointer system that allows the assistant to remember past interactions per user thread.

---

## 🚀 Key Engineering Highlights
* **Intelligent Routing:** Implemented a logical router that interprets user intent and dispatches tasks to dedicated expert agents.
* **Real-time RAG (Retrieval-Augmented Generation):** Integrated live web-searching to ground LLM responses in current, factual data (e.g., February 2026 updates).
* **Data Synthesis:** Engineered specific prompts that transform messy, unstructured search results into clean **Markdown Tables** and structured reports.
* **Persistent Sessions:** Leveraged SQLite to create a "thread-safe" memory, allowing the UI to maintain context across restarts.

---

## 🧠 Solved Challenges (The "Dev" Journey)
Working on the **"Bleeding Edge"** of Python 3.14 presented unique hurdles that I successfully resolved:
- **Async & Checkpointer Stability:** Fixed `GeneratorContextManager` errors by refactoring the `SqliteSaver` initialization to handle manual database connections.
- **Gradio 6.0 Migration:** Proactively updated the frontend architecture to match the latest 2026 standards for `ChatInterface` examples and parameter passing.
- **Dependency Orchestration:** Resolved Pydantic V1/V2 compatibility layers within the LangChain ecosystem.

---

## 📁 Project Structure
```text
personal_assistant_ai/
├── database/          # Persistent SQLite storage
├── graph/             # Workflow definitions, state, and agent nodes
│   ├── nodes.py       # Agent logic & prompt engineering
│   └── workflow.py    # LangGraph state machine definition
├── utils/             # Model & Tool initializers (Ollama, Tavily)
├── .env               # Protected API keys
├── main.py            # Gradio 6.0 UI and application entry point
└── requirements.txt   # Managed dependencies
⚙️ Installation & Usage
Clone the repository:

Bash
git clone [https://github.com/your-username/personal-assistant-ai.git](https://github.com/your-username/personal-assistant-ai.git)
cd personal-assistant-ai
Configure Environment:
Create a .env file and add your API key:

Απόσπασμα κώδικα
TAVILY_API_KEY=tvly-your-key-here
Initialize AI Models:
Ensure Ollama is installed and running:

Bash
ollama pull mistral
Launch Application:

Bash
pip install -r requirements.txt
python main.py
📬 Contact
Ilias Moratis AI Engineer | Python Developer 
