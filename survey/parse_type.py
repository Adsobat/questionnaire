from enum import Enum


class ParseType(Enum):
    QUESTION = 0
    WRONG_ANSWER = 1
    CORRECT_ANSWER = 2
    UNKNOWN = 3
