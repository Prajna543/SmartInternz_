from dotenv import load_dotenv
import os
import google.generativeai as genai

print("=" * 60)
print("Google Gemini API Key Test")
print("=" * 60)
print()

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ ERROR: GOOGLE_API_KEY not found in .env file")
    print()
    print("Please add your API key to the .env file:")
    print("GOOGLE_API_KEY=your_actual_api_key_here")
    print()
    exit(1)

if api_key == "your_api_key_here":
    print("❌ ERROR: Please replace 'your_api_key_here' with your actual API key")
    print()
    print("Get your API key from: https://ai.google.dev/gemini-api/docs/api-key")
    print()
    exit(1)

print(f"✅ API key found: {api_key[:20]}...")
print()

try:
    print("Testing connection to Google Gemini API...")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content("Say 'API test successful!' if you receive this message.")

    print("✅ Connection successful!")
    print()
    print("Response from Gemini AI:")
    print("-" * 60)
    print(response.text)
    print("-" * 60)
    print()
    print("🎉 Your API key is working correctly!")
    print()
    print("You can now run the main application:")
    print("streamlit run app.py")
    print()

except Exception as e:
    print("❌ ERROR: Failed to connect to Google Gemini API")
    print()
    print(f"Error details: {str(e)}")
    print()
    print("Possible solutions:")
    print("1. Check if your API key is correct")
    print("2. Verify your internet connection")
    print("3. Generate a new API key at: https://aistudio.google.com/")
    print("4. Make sure 'google-generativeai' package is installed")
    print()
    exit(1)

print("=" * 60)
