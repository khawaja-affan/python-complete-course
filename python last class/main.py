import os
import google.generativeai as genai

# Load API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY not found")
    print('Set it using: setx GEMINI_API_KEY "your_key"')
    exit()

# Configure Gemini
genai.configure(api_key=API_KEY)

# Create model & chat
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

print("🤖 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("exit", "quit"):
        print("👋 Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text, "\n")
    except Exception as e:
        print("⚠️ Error:", e)
        print("Please check your API key and internet.\n")
