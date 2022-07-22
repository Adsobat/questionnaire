from typing import List

from answer.anwser import Answer


def evaluate(answers: List[Answer]) -> (int, int):
    correctly_answered = 0
    max_questions = len(answers)

    for answers in answers:
        if answers.is_correct:
            correctly_answered += 1

    score = correctly_answered / max_questions if max_questions > 0 else 0
    return correctly_answered, score
