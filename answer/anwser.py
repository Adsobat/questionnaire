class Answer:
    question: str
    picked_answer: str
    is_correct: bool

    def __init__(self, question: str, picked_answer: str, correct_answer: str, is_correct: bool):
        self.correct_answer = correct_answer
        self.question = question
        self.is_correct = is_correct
        self.picked_answer = picked_answer
