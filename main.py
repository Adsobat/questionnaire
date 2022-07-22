# This is a sample Python script.
from ui import ui
from survey import survey_provider
from evaluator.question_evaluator import evaluate

QUESTION_PATH = "resources/questions.txt"


def main():
    questions = survey_provider.get_questions(path=QUESTION_PATH)
    answers = []
    for question in questions:
        question_answers = ui.ask_question(question)
        answers.append(question_answers)
    correctly_answered, score = evaluate(answers)
    ui.render_results(correctly_answered, score, answers)


if __name__ == '__main__':
    main()
