import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List, TextIO


@dataclass
class Questionnaire:
    """Simple immutable representation of a questionnaire."""
    id: str
    title: str
    questions: List[str]
    created_at: datetime


def parse_csv(file_obj: TextIO) -> List[Questionnaire]:
    """
    Parse a CSV (file‑object) containing questionnaires.

    Expected columns: id, title, questions (comma‑separated), created_at (ISO‑8601).
    """
    reader = csv.DictReader(file_obj)
    questionnaires: List[Questionnaire] = []

    for row in reader:
        # Split the "questions" column on commas, strip whitespace
        questions = [q.strip() for q in row["questions"].split(",")]
        questionnaires.append(
            Questionnaire(
                id=row["id"],
                title=row["title"],
                questions=questions,
                created_at=datetime.fromisoformat(row["created_at"]),
            )
        )
    return questionnaires