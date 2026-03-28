# agents/competitor.py

from typing import Any
from agents.base import BaseAgent


class CompetitorAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(
            name="competitor",
            role="Competitor analyst that compares key players."
        )

    def build_system_prompt(self) -> str:
        return (
            "You are a COMPETITOR ANALYST.\n"
            "You analyze key competitors in a market and compare them on strengths, "
            "weaknesses, positioning, and differentiation.\n"
            "You do not invent detailed financials; you stay high-level but concrete."
        )

    def build_user_prompt(self, **kwargs: Any) -> str:
        question: str = kwargs["question"]
        research_notes: str = kwargs["research_notes"]
        return (
            f"The user's original market research question is:\n{question}\n\n"
            "You are given raw market research notes:\n"
            f"{research_notes}\n\n"
            "From this, identify 3–7 key competitors and compare them on:\n"
            "- Target segment\n- Value proposition\n- Strengths\n- Weaknesses\n"
            "- Differentiation\n\n"
            "Respond in markdown with:\n"
            "## Competitor list\n"
            "## Detailed comparison\n"
        )