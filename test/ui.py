from unittest import TestCase
from ui import ui
from survey.survey_element import SurveyElement


class UI(TestCase):
    def test_render_question(self):
        question = SurveyElement()
        question.question = "What is your house like?"
        question.add_wrong_answer("curly")
        question.add_wrong_answer("big")
        question.add_right_answer("cheap")

        question_str = ui.render_question(question)

        self.assertEqual("What is your house like?", question_str[0])
        self.assertEqual("1) curly", question_str[1])
        self.assertEqual("2) big", question_str[2])
        self.assertEqual("3) cheap", question_str[3])

    def test__strip_characters(self):
        txt = "1) \n"

        answer = ui._strip_characters(txt, [")", " ", "\n"])

        self.assertEqual("1", answer)

    def test__strip_characters__empty_character_list(self):
        txt = "1) \n"

        answer = ui._strip_characters(txt, [])

        self.assertEqual("1) \n", answer)

    def test__strip_characters__empty_text(self):
        txt = ""

        answer = ui._strip_characters(txt, ["a"])

        self.assertEqual("", answer)
