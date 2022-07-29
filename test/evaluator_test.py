from unittest import TestCase
from answer.anwser import Answer
from evaluator.question_evaluator import evaluate


class Evaluator(TestCase):
    def test_evaluate__correct_answers(self):
        answers = [Answer("q", "yes", "yes", True)]

        correctly_answered, points = evaluate(answers)

        self.assertEqual(1, correctly_answered)
        self.assertEqual(100, points)

    def test_evaluate__wrong_answers(self):
        answers = [Answer("q", "yes", "no", False)]

        correctly_answered, points = evaluate(answers)

        self.assertEqual(0, correctly_answered)
        self.assertEqual(0.0, points)

    def test_evaluate__points_score(self):
        answers = [Answer("q", "yes", "no", False),
                   Answer("q", "yes", "yes", True)]

        _, points = evaluate(answers)

        self.assertEqual(50.0, points)

    def test_evaluate__no_answers(self):
        answers = []

        correct_answers, points = evaluate(answers)

        self.assertEqual(0.0, points)
        self.assertEqual(0, correct_answers)
