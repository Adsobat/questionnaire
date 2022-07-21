from unittest import TestCase

from Survey.question import Question


class QuestionCreation(TestCase):

    def test_add_answer(self):
        question = Question()

        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")
        question.add_wrong_answer("a3")
        question.add_wrong_answer("a3")

        self.assertEqual("a1", question.answer[0])
        self.assertEqual("a2", question.answer[1])
        self.assertEqual("a3", question.answer[2])

    def test_add_right_answer_beginning(self):
        q = Question()
        q.add_right_answer("hello")
        q.add_wrong_answer("wrong")
        q.add_wrong_answer("wrong2")
        self.assertEqual(0, q._correct_answer_index)

    def test_add_right_answer__add_to_multiple_answers(self):
        question = Question()
        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")
        question.add_right_answer("right")
        question.add_wrong_answer("a3")

        right_answer = question.get_correct_answer()

        self.assertEqual("right", right_answer)

    def test_add_wrong_answer(self):
        question = Question()
        question.add_wrong_answer("a1")
        question.add_wrong_answer("a2")

        self.assertEqual(2, len(question.answer))
        self.assertEqual("a1", question.answer[0])
        self.assertEqual("a2", question.answer[1])

    def test_is_valid_question(self):
        question = Question()

        question.question = "question?"
        question.add_right_answer("right")
        question.add_wrong_answer("a1")

        self.assertTrue(question.is_valid_question())

    def test_is_valid_question__no_answer(self):
        question = Question()
        question.question = "hallo"
        question.add_wrong_answer("a1")

        before_adding_answer = question.is_valid_question()
        question.add_right_answer("right")

        self.assertFalse(before_adding_answer)
        self.assertTrue(question.is_valid_question())

    def test_is_valid_question__wrong_correct_answer_index(self):
        question = Question()
        question.question = "hallo"
        question.add_wrong_answer("a1")
        question.add_right_answer("right")

        is_valid_question = question.is_valid_question()
        question.answer = question.answer[0:1]
        after_wrong_index = question.is_valid_question()

        self.assertFalse(after_wrong_index)
        self.assertTrue(is_valid_question)

    def test_is_valid_question__no_question_set(self):
        question = Question()
        question.add_wrong_answer("a1")
        question.add_right_answer("right")

        before_valid_question = question.is_valid_question()
        question.question = "hallo"
        after_valid_question = question.is_valid_question()

        self.assertFalse(before_valid_question)
        self.assertTrue(after_valid_question)
