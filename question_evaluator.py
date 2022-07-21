from typing import List

from anwser import Answer


def evaluate(answers: List[Answer]) -> (int, int):
    correctly_answered = 0
    max_questions = len(answers)

    for answers in answers:
        if answers.is_correct:
            correctly_answered += 1

    points = correctly_answered / max_questions
    return correctly_answered, points
