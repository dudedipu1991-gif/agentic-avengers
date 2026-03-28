# agents/analyst.py

from typing import Any
from agents.base import BaseAgent


class AnalystAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            name="analyst",
            role="Market analyst that synthesizes a final report."
        )

    def build_system_prompt(self) -> str:
        return (
            "You are a MARKET ANALYST.\n"
            "You synthesize research and competitor analysis into a concise, "
            "executive-style market research report."
        )

    def build_user_prompt(self, **kwargs: Any) -> str:
        question: str = kwargs["question"]
        research_notes: str = kwargs["research_notes"]
        competitor_notes: str = kwargs.get("competitor_notes", "")

        return (
            f"User question:\n{question}\n\n"
            "Raw research notes:\n"
            f"{research_notes}\n\n"
            "Competitor analysis (may be empty):\n"
            f"{competitor_notes}\n\n"
            "Write a clear market research report in markdown with sections:\n"
            "## Executive summary (4–6 sentences)\n"
            "## Market overview\n"
            "## Customer segments\n"
            "## Key competitors and positioning\n"
            "## Trends, opportunities, and risks\n\n"
            "Keep it under about 1000 words and avoid repeating the same sentences."
        )