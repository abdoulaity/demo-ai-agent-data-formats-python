import os
from dotenv import load_dotenv

# Loading the Anthropic key
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

print(f"Key successfully loaded : {api_key[:5]}...") 

# Initializing the Model
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    temperature=0.75,
    max_tokens=1000,
    )