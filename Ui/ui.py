from typing import List

from anwser import Answer
from Survey.question import Question


def ask_question(survey_element: Question) -> Answer:
    question_console_representation = render_question(survey_element)
    render_text(question_console_representation)
    picked_answer_number = _get_user_input(1, len(survey_element.answer))
    picked_answer = survey_element.answer[picked_answer_number - 1]
    is_correct = survey_element.get_correct_answer_number() == picked_answer_number
    return Answer(question=survey_element.question, picked_answer=picked_answer, is_correct=is_correct)


def _get_user_input(min_value: int, max_value: int):
    user_input = -1
    while not _is_valid_question_answer(min_value, max_value, user_input):
        user_input = _get_number_from_user("Please choose an Answer by typing the correct number \n")
    return user_input


def _is_valid_question_answer(min_value, max_value, user_input) -> bool:
    return min_value <= user_input <= max_value


def _get_number_from_user(input_txt: str) -> int:
    while True:
        result = input(input_txt)
        result = _strip_characters(result, [")", " ", "\n"])
        if result.isdigit():
            return int(result)


def _strip_characters(txt, characters) -> str:
    for c in characters:
        txt = txt.replace(c, "")
    return txt


def render_text(lines: List[str]):
    for line in lines:
        print(line)


def render_question(survey_element: Question) -> List[str]:
    question_text = survey_element.question
    answers = [f"{i + 1}) {txt}" for i, txt in enumerate(survey_element.answer)]

    return [question_text] + answers


def _print_score(correctly_answered, points, questions_amount):
    print(f"you got {correctly_answered} / {questions_amount} right ({points}%)")


def render_results(correctly_answered: int, points: int, answers: List[Answer]):
    _print_score(correctly_answered, points, len(answers))
    _render_answers_result(answers)
    return None


def _render_answers_result(answers: List[Answer]):
    for answer in answers:
        print(answer.question)
        if answer.is_correct:
            print(f" Your answer {answer.picked_answer} is correct")
        else:
            print(f" Your answer {answer.picked_answer} is wrong")
