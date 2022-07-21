# This is a sample Python script.
from Ui import ui
from Survey import question_provider
from question_evaluator import evaluate
QUESTION_PATH = "resources/questions.txt"
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    questions = question_provider.get_questions(path=QUESTION_PATH)
    answers = []
    for question in questions:
        question_answers = ui.ask_question(question)
        answers.append(question_answers)
    correctly_answered, points = evaluate(answers)
    ui.render_results(correctly_answered, points, answers)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
