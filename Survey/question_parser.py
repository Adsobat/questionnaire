from enum import Enum
from typing import List

from Survey.question import Question

QUESTION_MARKER = "?"
CORRECT_ANSWER_MARKER = "*"


def parse(raw_file: List[str]) -> List[Question]:
    result = []
    tmp_question: Question = Question()
    for line in raw_file:
        line, is_question = _parse_for_question(line)
        if is_question:
            if tmp_question.is_valid_question():
                result.append(tmp_question)
            tmp_question = Question()
            tmp_question.question = line
        else:
            line, is_correct_answer = _parse_answer(line)
            if is_correct_answer:
                tmp_question.add_right_answer(line)
            else:
                tmp_question.add_wrong_answer(line)
    if tmp_question.is_valid_question():
        result.append(tmp_question)
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
