from typing import List


class Question(object):
    question: str
    answer: List[str]
    _correct_answer_index: int

    def __init__(self):
        self.question = ""
        self.answer = []
        self._correct_answer_index = -1

    def add_wrong_answer(self, answer: str):
        if len(answer) > 0:
            self.answer.append(answer)

    def add_right_answer(self, answer):
        if len(answer) > 0:
            self.answer.append(answer)
            self._correct_answer_index = len(self.answer) - 1

    def is_valid_question(self) -> bool:
        has_answer = self._correct_answer_index >= 0
        is_possible_answer = self._correct_answer_index < len(self.answer)
        has_question = len(self.question) > 0
        return has_question and is_possible_answer and has_answer

    def get_correct_answer(self):
        return self.answer[
            self._correct_answer_index] if 0 < self._correct_answer_index < len(self.answer) else ""

    def get_correct_answer_number(self):
        return self._correct_answer_index + 1