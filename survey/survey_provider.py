from typing import List

from survey import survey_parser
from survey.survey_element import SurveyElement


def get_questions(path: str) -> List[SurveyElement]:
    with open(path) as file:
        lines = file.readlines()
        lines = _strip_new_lines_at_end(lines)
        questions = survey_parser.parse(lines)
    return questions


def _strip_new_lines_at_end(lines: List[str]):
    return [line[:-1] if line[-1] == "\n" else line for line in lines]
