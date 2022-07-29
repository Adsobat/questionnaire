from typing import List


class SurveyElement(object):
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

    def add_correct_answer(self, answer):
        if len(answer) > 0:
            self.answer.append(answer)
            self._correct_answer_index = len(self.answer) - 1

    def get_correct_answer(self):
        return self.answer[
            self._correct_answer_index] if 0 <= self._correct_answer_index < len(self.answer) else ""

    def get_correct_answer_number(self):
        return self._correct_answer_index + 1
