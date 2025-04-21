# 🎙️ Voice-Based AI Agent for Windows

This project is a Python-based AI agent that converts voice commands into Windows shell commands.  
It integrates **Whisper** for speech-to-text transcription and **Mistral LLM** (via LangChain)  
to understand and generate accurate command-line instructions for file operations and system tasks.  
Designed with modularity in mind, it enables users to speak commands and get ready-to-execute Windows shell commands as output.

## 🚀 Features
- 🎤 Convert voice to executable Windows shell commands
- 🤖 Powered by OpenAI Whisper and Mistral LLM
- 📁 Handles file operations like copy, move, and delete
- 🧠 Uses natural language understanding to reduce command misinterpretation
- 🧩 Modular structure for easy extension (e.g., chatbot, RAG)
- 📈 85% command execution success rate

## 🧠 Tech Stack
- Python 3.8+
- [Whisper (openai-whisper)](https://github.com/openai/whisper)
- [LangChain](https://www.langchain.com/)
- [Mistral LLM](https://mistral.ai/) via langchain_mistralai
- Windows-compatible shell commands


## 📦 Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/ayushdev234/Voice-based-AI-agent-for-window.git
    cd Voice-based-AI-agent-for-window
    ```

2. **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🔐 API Key Setup
Before using Mistral via LangChain, set the API key:

```bash
# Windows
set MISTRAL_API_KEY=your_api_key

# macOS/Linux
export MISTRAL_API_KEY=your_api_key
