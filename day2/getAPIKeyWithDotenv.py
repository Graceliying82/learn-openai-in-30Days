import os
from dotenv import load_dotenv

load_dotenv()
openAI_api_key = os.getenv("OPENAI_API_KEY")

# Add Add API-Keys to .env