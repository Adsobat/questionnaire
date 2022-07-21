from unittest import TestCase

from Survey.question_parser import parse
SINGLE_SURVEY = ["?Which of these animals is a mammal",
                 "Ant",
                 "Bee",
                 "*Cat"]
LONG_SURVEY = ["?Which of these animals is a mammal",
               "Ant",
               "Bee",
               "*Cat",
               "?How old are you",
               "*99",
               "123",
               "312"]


class QuestionParser(TestCase):

    def test_parse_single_question(self):
        questions = parse(SINGLE_SURVEY)

        self.assertEqual(1, len(questions))
        self.assertEqual("Which of these animals is a mammal", questions[0].question)
        self.assertEqual("Cat", questions[0].answer[questions[0]._correct_answer_index])

    def test_parse_multiple_question(self):
        questions = parse(LONG_SURVEY)

        self.assertEqual(2, len(questions))
        self.assertEqual("Which of these animals is a mammal", questions[0].question)
        self.assertEqual("Cat", questions[0].answer[questions[0]._correct_answer_index])
        self.assertEqual("How old are you", questions[1].question)
        self.assertEqual("99", questions[1].answer[questions[1]._correct_answer_index])

    def test_parse_empty_question_list(self):
        questions = parse([])

        self.assertEqual(0, len(questions))

    def test_parse_faulty_question__no_correct_anwser(self):
        single_faulty_survey = ["?what is love", "a gun", "a bear"]
        question = parse(single_faulty_survey)

        self.assertEqual(0, len(question))



