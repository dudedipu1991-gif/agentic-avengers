# core/orchestration.py

from agents.researcher import ResearcherAgent
from agents.competitor import CompetitorAgent
from agents.analyst import AnalystAgent


class MarketResearchWorkflow:
    """Researcher → Competitor (optional) → Analyst."""

    def __init__(self, use_competitor: bool = True) -> None:
        self.researcher = ResearcherAgent()
        self.use_competitor = use_competitor
        self.competitor = CompetitorAgent() if use_competitor else None
        self.analyst = AnalystAgent()

    def run(self, question: str) -> dict:
        # 1. Research
        research_notes = self.researcher.run(question=question)

        # 2. Competitor analysis (optional)
        competitor_notes = ""
        if self.use_competitor and self.competitor is not None:
            competitor_notes = self.competitor.run(
                question=question,
                research_notes=research_notes,
            )

        # 3. Final report
        report = self.analyst.run(
            question=question,
            research_notes=research_notes,
            competitor_notes=competitor_notes,
        )

        return {
            "research_notes": research_notes,
            "competitor_notes": competitor_notes,
            "report": report,
        }