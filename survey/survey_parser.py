from enum import Enum
from typing import List

from survey.survey_element import SurveyElement

QUESTION_MARKER = "?"
CORRECT_ANSWER_MARKER = "*"


def parse(raw_file: List[str]) -> List[SurveyElement]:
    result = []
    parsed_element: SurveyElement = SurveyElement()
    for line in raw_file:
        line, is_question = _parse_for_question(line)
        if is_question:
            if parsed_element.is_valid_question():
                result.append(parsed_element)
            parsed_element = SurveyElement()
            parsed_element.question = line
        else:
            line, is_correct_answer = _parse_answer(line)
            if is_correct_answer:
                parsed_element.add_right_answer(line)
            else:
                parsed_element.add_wrong_answer(line)
    if parsed_element.is_valid_question():
        result.append(parsed_element)
    return result


def _parse_for_question(line: str) -> (str, bool):
    if len(line) <= 0:
        return "", False
    is_question = line[0] == QUESTION_MARKER
    return line[1:] if is_question else line, is_question


def _parse_answer(line: str):
    if len(line) <= 0:
        return "", False
    is_correct = line[0] == CORRECT_ANSWER_MARKER
    return line[1:] if is_correct else line, is_correct
