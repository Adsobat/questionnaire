from unittest import TestCase

from survey.survey_element import SurveyElement


class QuestionCreation(TestCase):

    def test_add_answer(self):
        question = SurveyElement()

        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")
        question.add_wrong_answer("a3")
        question.add_wrong_answer("a3")

        self.assertEqual("a1", question.answer[0])
        self.assertEqual("a2", question.answer[1])
        self.assertEqual("a3", question.answer[2])

    def test_add_right_answer_beginning(self):
        q = SurveyElement()
        q.add_correct_answer("hello")
        q.add_wrong_answer("wrong")
        q.add_wrong_answer("wrong2")
        self.assertEqual(0, q._correct_answer_index)

    def test_add_right_answer__add_to_multiple_answers(self):
        question = SurveyElement()
        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")
        question.add_correct_answer("right")
        question.add_wrong_answer("a3")

        right_answer = question.get_correct_answer()

        self.assertEqual("right", right_answer)

    def test_add_wrong_answer(self):
        question = SurveyElement()
        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")

        self.assertEqual(2, len(question.answer))
        self.assertEqual("a1", question.answer[0])
        self.assertEqual("a2", question.answer[1])


