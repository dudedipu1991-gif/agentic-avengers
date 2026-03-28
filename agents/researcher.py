# agents/researcher.py

from typing import Any
from agents.base import BaseAgent


class ResearcherAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            name="researcher",
            role="Market researcher that gathers factual information."
        )

    def build_system_prompt(self) -> str:
        return (
            "You are a MARKET RESEARCHER.\n"
            "You gather up-to-date, factual information about markets, industries, "
            "and companies. When unsure, explicitly say what is uncertain.\n"
            "Use clear headings and bullet points where useful."
        )

    def build_user_prompt(self, **kwargs: Any) -> str:
        question: str = kwargs["question"]
        return (
            f"Task: Collect factual information for this market research query:\n\n"
            f"\"{question}\"\n\n"
            "Focus on the following:\n"
            "- Market size and growth\n"
            "- Key segments and use cases\n"
            "- Key players\n"
            "- Customer types and geographies\n"
            "- Recent trends in the last 2–3 years\n\n"
            "Return structured notes, not final recommendations."
        )