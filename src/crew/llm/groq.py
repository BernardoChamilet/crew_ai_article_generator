from crewai import LLM
from src.config.config import groq_api_key

# Configurando a LLM
llm_groq = LLM(
    model="groq/llama3-8b-8192",
    api_key=groq_api_key,
    temperature=0.7
)
