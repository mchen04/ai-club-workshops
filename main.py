import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API key
genai.configure(api_key=API_KEY)

# Use Gemini 1.5 Flash for efficiency
model = genai.GenerativeModel("gemini-1.5-flash")

def ai_therapist():
    print("Welcome to AI Therapist. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Therapist: Take care! Goodbye!")
            break
        response = model.generate_content([user_input], generation_config={"max_output_tokens": 100})
        print("AI Therapist:", response.text)

# Run the chatbot
ai_therapist()