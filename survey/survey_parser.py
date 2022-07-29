from enum import Enum
from typing import List

from survey.parse_type import ParseType
from survey.survey_element import SurveyElement

QUESTION_MARKER = "?"
CORRECT_ANSWER_MARKER = "*"
UNKNOWN_ANSWER = "I don't know."


def parse(raw_file: List[str]) -> List[SurveyElement]:
    result = []
    parsed_element: SurveyElement = SurveyElement()
    for line in raw_file:
        line, line_type = _parse_line(line)
        if line_type == ParseType.QUESTION:
            _add_element(parsed_element, result)
            parsed_element = SurveyElement()
            parsed_element.question = line
        elif line_type == ParseType.WRONG_ANSWER:
            parsed_element.add_wrong_answer(line)
        elif line_type == ParseType.CORRECT_ANSWER:
            parsed_element.add_correct_answer(line)

    _add_element(parsed_element, result)
    return result


def is_valid_question(question: SurveyElement) -> bool:
    has_answer = question.get_correct_answer() != ""
    has_question = len(question.question) > 0
    return has_question and has_answer


def _add_element(parsed_element, result):
    if is_valid_question(parsed_element):
        parsed_element.add_wrong_answer(UNKNOWN_ANSWER)
        result.append(parsed_element)


def _parse_line(line: str) -> (str, ParseType):
    if len(line) <= 0:
        return "", ParseType.UNKNOWN
    line, is_question = _parse_for_question(line)
    if is_question:
        return line, ParseType.QUESTION
    line, is_correct = _parse_answer(line)
    if is_correct:
        return line, ParseType.CORRECT_ANSWER
    else:
        return line, ParseType.WRONG_ANSWER


def _parse_for_question(line: str) -> (str, bool):
    is_question = line[0] == QUESTION_MARKER
    if line[-1] != QUESTION_MARKER and is_question:
        line += QUESTION_MARKER
    return line[1:] if is_question else line, is_question


def _parse_answer(line: str):
    is_correct = line[0] == CORRECT_ANSWER_MARKER
    return line[1:] if is_correct else line, is_correct
