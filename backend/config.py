"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-5.6-luna-pro",
    "google/gemini-3.8-flash",
    "anthropic/claude-opus-5.5",
    "~x-ai/grok-latest",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "openai/gpt-5.6-luna-pro"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
