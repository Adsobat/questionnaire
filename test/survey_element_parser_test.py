from unittest import TestCase

from survey.survey_element import SurveyElement
from survey.survey_parser import parse
from survey import survey_parser
SINGLE_SURVEY = ["?Which of these animals is a mammal",
                 "Ant",
                 "Bee",
                 "*Cat"]
LONG_SURVEY = ["?Which of these animals is a mammal",
               "Ant",
               "Bee",
               "*Cat",
               "?How old are you?",
               "*99",
               "123",
               "312"]


class QuestionParser(TestCase):

    def test_parse_single_question(self):
        questions = parse(SINGLE_SURVEY)

        self.assertEqual(1, len(questions))
        self.assertEqual("Which of these animals is a mammal?", questions[0].question)
        self.assertEqual("Cat", questions[0].get_correct_answer())

    def test_parse_multiple_question(self):
        questions = parse(LONG_SURVEY)

        self.assertEqual(2, len(questions))
        self.assertEqual("Which of these animals is a mammal?", questions[0].question)
        self.assertEqual("Cat", questions[0].get_correct_answer())
        self.assertEqual("How old are you?", questions[1].question)
        self.assertEqual("99", questions[1].get_correct_answer())

    def test_parse_empty_question_list(self):
        questions = parse([])

        self.assertEqual(0, len(questions))

    def test_parse_faulty_question__no_correct_anwser(self):
        single_faulty_survey = ["?what is love", "a gun", "a bear"]
        question = parse(single_faulty_survey)

        self.assertEqual(0, len(question))

    def test_is_valid_question(self):
        question = SurveyElement()

        question.question = "question?"
        question.add_correct_answer("right")
        question.add_wrong_answer("a1")

        self.assertTrue(survey_parser.is_valid_question(question))

    def test_is_valid_question__no_answer(self):
        question = SurveyElement()
        question.question = "hallo"
        question.add_wrong_answer("a1")

        before_adding_answer = survey_parser.is_valid_question(question)

        question.add_correct_answer("right")

        self.assertFalse(before_adding_answer)
        self.assertTrue(survey_parser.is_valid_question(question))

    def test_is_valid_question__wrong_correct_answer_index(self):
        question = SurveyElement()
        question.question = "hallo"
        question.add_wrong_answer("a1")
        question.add_correct_answer("right")

        is_valid_question = survey_parser.is_valid_question(question)
        question.answer = question.answer[0:1]
        after_wrong_index = survey_parser.is_valid_question(question)

        self.assertFalse(after_wrong_index)
        self.assertTrue(is_valid_question)

    def test_is_valid_question__no_question_set(self):
        question = SurveyElement()
        question.add_wrong_answer("a1")
        question.add_correct_answer("right")

        before_valid_question = survey_parser.is_valid_question(question)
        question.question = "hallo"
        after_valid_question = survey_parser.is_valid_question(question)

        self.assertFalse(before_valid_question)
        self.assertTrue(after_valid_question)


