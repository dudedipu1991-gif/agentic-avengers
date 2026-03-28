# config/settings.py

import os
from dataclasses import dataclass
# from config.settings import GROQ_CONFIG, get_groq_api_key

@dataclass
class GroqConfig:
    model: str = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")
    temperature: float = float(os.getenv("GROQ_TEMPERATURE", "0.2"))
    max_tokens: int = int(os.getenv("GROQ_MAX_TOKENS", "2000"))


GROQ_CONFIG = GroqConfig()


def get_groq_api_key() -> str:
    key = os.getenv("GROQ_API_KEY", "")
    if not key:
        raise ValueError("GROQ_API_KEY not set.")
    return key