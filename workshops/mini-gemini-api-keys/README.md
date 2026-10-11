## Running from this collection

From the collection root, enter `workshops/mini-gemini-api-keys`. Create a separate environment (dependency imports checked with Python 3.12):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The original setup and `python main.py` command below apply from this directory. Hosted Gemini requests were not tested: they need the learner's own key and an available model. This historical example retains the `google-generativeai` SDK and `gemini-1.5-flash`; that model may be unavailable, and no migration to a newer integration is included. The retained SDK emits an end-of-support warning when imported. Installing/importing the dependencies does not prove hosted generation works. No key is supplied by this collection. Keep `.env` local and untracked.

---

# Mini Workshop: Introduction to API Keys with the Gemini API

## Introduction
This AI Club mini workshop shows how to use an API key to call a hosted AI model. You build a small command line chatbot, the "AI Therapist", with Google's Gemini API. Along the way you learn how to keep a secret key out of your source code by loading it from a `.env` file.

## What You Will Learn
- What an API key is and why each request needs one.
- How to store a key in a `.env` file and read it with `python-dotenv`.
- How to configure the `google-generativeai` client and select a model.
- How to send a prompt and print the model's reply in a chat loop.

## Why You Need an API Key
The Gemini model does not run on your computer. Your script sends each message to Google's servers. The API key identifies your account, so Google can authorize the request, apply your quota, and bill usage. Without a valid key the request fails.

Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Setup

### 1. Install the dependencies
```
pip install google-generativeai python-dotenv
```

### 2. Create your `.env` file
Create a file named `.env` next to `main.py` and add your key:
```
GEMINI_API_KEY=your_key_here
```
The `.gitignore` excludes `.env`, so your key stays out of git. Never commit a key.

### 3. Run the script
```
python main.py
```

## Usage
Type a message and press Enter. The model answers as the AI Therapist. Type `exit` to stop.

The script uses the `gemini-1.5-flash` model and caps each reply at 100 output tokens to keep responses fast and cheap.

## Social Links
 - Discord: https://discord.gg/tmd2hQE4SK
 - Instagram: https://www.instagram.com/ucrai_/
 - Highlander Link: https://highlanderlink.ucr.edu/organization/ai_at_ucr
 - LinkedIn: https://www.linkedin.com/company/ai-at-ucr/
