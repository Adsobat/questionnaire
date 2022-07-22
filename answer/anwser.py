class Answer:
    question: str
    picked_answer: str
    is_correct: bool

    def __init__(self, question: str, picked_answer: str, is_correct: bool):
        self.question = question
        self.is_correct = is_correct
        self.picked_answer = picked_answer
