# agents/base.py

from __future__ import annotations

import abc
from typing import Any, Dict, List

from groq import Groq
from config.settings import GROQ_CONFIG, get_groq_api_key  # <- important


_client = Groq(api_key=get_groq_api_key())


class BaseAgent(abc.ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.model = GROQ_CONFIG.model
        self.temperature = GROQ_CONFIG.temperature

    @abc.abstractmethod
    def build_system_prompt(self) -> str:
        ...

    @abc.abstractmethod
    def build_user_prompt(self, **kwargs: Any) -> str:
        ...

    def call_llm(self, messages: List[Dict[str, str]]) -> str:
        resp = _client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=GROQ_CONFIG.max_tokens,
        )
        return resp.choices[0].message.content.strip()

    def run(self, **kwargs: Any) -> str:
        system_prompt = self.build_system_prompt()
        user_prompt = self.build_user_prompt(**kwargs)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        return self.call_llm(messages)