import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Configurando a LLM Gemini
llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)
