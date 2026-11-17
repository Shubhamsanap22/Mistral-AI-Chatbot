# Mistral AI Chatbot

## Project Overview

This project is an interactive AI chatbot built using **Python, Mistral AI, LangChain, and Streamlit**. It allows users to interact with an AI language model through a web-based chat interface.

The chatbot supports different conversational personalities, allowing users to experience responses with different tones.

## Features

- **Mistral AI Integration:** Uses the Mistral language model to generate responses.
- **Multiple Personality Modes:** Supports Angry, Funny, and Sad conversational styles.
- **Interactive Chat Interface:** Provides a user-friendly interface using Streamlit.
- **Conversation History:** Maintains chat history during the application session.
- **Custom UI:** Includes custom CSS styling for an improved user experience.
- **Prompt Engineering:** Uses personality-based system prompts to control response tone.

## Technologies Used

- Python
- Mistral AI API
- LangChain
- Streamlit
- CSS
- Python-dotenv

## Project Structure

```text
Mistral-AI-Chatbot/
│
├── chatmodels/
│   ├── chat.py
│   └── uichat.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shubhamsanap22/Mistral-AI-Chatbot.git
```

### 2. Navigate to the project directory

```bash
cd Mistral-AI-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Mistral API key

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Replace the placeholder with your own API key. Never upload this file to GitHub.

### 6. Run the application

If `uichat.py` is the main Streamlit application:

```bash
streamlit run chatmodels/uichat.py
```

## Learning Outcomes

- Integrating Large Language Models into Python applications.
- Working with Mistral AI through LangChain.
- Implementing prompt engineering and personality-based responses.
- Developing interactive applications using Streamlit.
- Managing conversational context and session state.
- Applying custom CSS to improve application interfaces.

## Future Improvements

- Add document-based question answering using RAG.
- Support conversation export and download.
- Add additional personality modes.
- Improve conversation memory and context management.

## Author

**Shubham Sanap**

M.Tech Data Science | COEP Technological University

[GitHub](https://github.com/Shubhamsanap22) · [LinkedIn](https://www.linkedin.com/in/shubham-sanap-b7298224b/)

---

*An interactive Generative AI application developed to explore LLM integration, prompt engineering, and conversational AI.*
