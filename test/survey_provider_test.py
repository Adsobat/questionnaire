from unittest import TestCase

from survey import survey_provider

TEST_DATA_PATH = "test/resources/test_data.txt"


class QuestionProvider(TestCase):

    def test_get_questions__amount(self):
        questions = survey_provider.get_questions(path=TEST_DATA_PATH)

        self.assertEqual(3, len(questions))

    def test_get_questions__correct_question_parse(self):
        questions = survey_provider.get_questions(path=TEST_DATA_PATH)

        question_texts = [q.question for q in questions]

        self.assertEqual("Which of these animals is a mammal?", question_texts[0])
        self.assertEqual("How old are you?", question_texts[1])
        self.assertEqual("What is your favorite color?", question_texts[2])

    def test_get_questions__correct_answer_parse(self):
        questions = survey_provider.get_questions(path=TEST_DATA_PATH)

        question_answers = [q.answer for q in questions]

        self.assertEqual(["Ant", "Bee", "Cat", "I don't know."], question_answers[0])
        self.assertEqual(["99", "123", "312", "I don't know."], question_answers[1])
        self.assertEqual(["blue", "green", "yellow", "apple", "I don't know."], question_answers[2])

