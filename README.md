# 🤖 AI Chat Bot

A conversational AI chat bot powered by Google's Gemini AI model, built with Streamlit and LangChain.

## Features

- 💬 Natural conversation with AI
- 🧠 Powered by Google Gemini 2.0 Flash
- 💾 Chat history preservation
- 🎨 Clean and intuitive UI
- ⚡ Fast and responsive

## Prerequisites

- Python 3.11+
- Google API Key (Gemini)

## Installation

1. Clone or download this repository

2. Create a virtual environment (if not already created):
```powershell
python -m venv venv
```

3. Activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:
```powershell
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_key_here  # Optional
HUGGINGFACEHUB_ACCESS_TOKEN=your_hf_token_here  # Optional
```

## Usage

### Run the Streamlit Chat App

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Run the app
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Run the Basic Script

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the script
python ChatModel\3_chatmodel_gemini.py
```

## Project Structure

```
AI_Chat_Bot/
├── app.py                          # Streamlit chat application
├── ChatModel/
│   └── 3_chatmodel_gemini.py      # Basic Gemini script
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (API keys)
├── venv/                           # Virtual environment
└── README.md                       # This file
```

## Available Models

- **Google Gemini** - gemini-2.0-flash-exp (default in app)
- **OpenAI** - GPT models (if API key provided)
- **Anthropic** - Claude models (if API key provided)
- **Hugging Face** - Various open-source models

## Tips

- Use the **Clear Chat History** button in the sidebar to start a fresh conversation
- The app maintains conversation context automatically
- All messages are stored in the session state

## Troubleshooting

**Import errors**: Make sure you've activated the virtual environment before running the app

**API errors**: Check that your `.env` file contains valid API keys

**Permission errors**: Run PowerShell as Administrator if you encounter installation issues

## Security Notes

⚠️ **IMPORTANT**: Never commit your `.env` file to version control. Make sure it's listed in `.gitignore`

## License

This project is for educational purposes.
