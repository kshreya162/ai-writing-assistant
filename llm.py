import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def get_llm(temperature=0.7):
    return ChatGoogleGenerativeAI(model="gemini-3.6-flash",
    temperature=temperature,
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    return llm

