from typing import List

from Survey import question_parser
from Survey.question import Question


def get_questions(path: str) -> List[Question]:
    with open(path) as file:
        lines = file.readlines()
        lines = _strip_new_lines_at_end(lines)
        questions = question_parser.parse(lines)
    return questions


def _strip_new_lines_at_end(lines: List[str]):
    return [line[:-1] if line[-1] == "\n" else line for line in lines]
