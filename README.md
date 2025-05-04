# QNA Chatbot

QNA Chatbot is a Streamlit-based application that uses Google's Gemini LLM to answer user questions interactively.

## Features

- Ask questions and get responses from the Gemini LLM.
- View chat history for the current session.
- Simple and user-friendly interface.

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/uv-org/uv) for managing environments and dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/qna-chatbot.git
   cd qna-chatbot
   ```

2. Install `uv` if not already installed:
   ```bash
   pip install uv
   ```

3. Create and activate the environment:
   ```bash
   uv venv
   ```

4. Install the required dependencies:
   ```bash
   uv add -r requirements.txt
   ```

## Usage

1. Set up your Google Gemini API key in the `.env` file:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

2. Run the application:
   ```bash
   streamlit run qnachat.py
   ```

3. Open the application in your browser at `http://localhost:8501`.

## File Structure

- `qnachat.py`: Main application file.
- `.env`: Stores the API key for Gemini LLM.
- `pyproject.toml`: Project metadata and dependencies.
- `requirements.txt`: List of dependencies.
- `.python-version`: Specifies the Python version.
