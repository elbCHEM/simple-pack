"""
Very simple io.
"""
import os
from typing import LiteralString, Optional


class MaximumQuestionsAnswerWrong(Exception):
    """Called when a question to the user has been answered wrong too many times"""
    question_asked: Optional[int] = None

    def __init__(self, *args, question_asked: Optional[int] = None):
        self.question_asked = question_asked
        super().__init__(*args)


_MAXIMUM_NUMBER_OF_QUESTIONS_ASKED = 100


def append_a_little_message_to_a_file(message: LiteralString, file: os.PathLike) -> None:
    """Print a little message to a file in append mode"""
    if not os.path.isfile(file):
        raise FileNotFoundError(f"File {file} does not exists")
    with open(file, mode="a") as filewrapper:
        filewrapper.writelines([message, ])


def get_integer_from_user_input(max_questions: int = _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED) -> Optional[int]:
    """Ask the user to provide an integer using the standard input. Empty answer if interpreted as exit.

    Args:
        max_questions (int, optional): Maximum number of wrong answers. Defaults to MAXIMUM_NUMBER_OF_QUESTIONS_ASKED.

    Raises:
        MaximumQuestionsAnswerWrong: If the user does not provide a valid answer too many times.

    Returns:
        Optional[int]: Integer that was provided by the user. None is no answer was provided.
    """
    max_questions = min(max_questions, _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED)

    for n in range(1, max_questions+1):
        raw_user_input = input("Please enter an integer: ")

        if not raw_user_input:
            return None
        if not (user_input := raw_user_input.strip()):
            print("Cannot interpret whitespace - Please try again")
            continue

        try:
            return int(user_input)
        except ValueError:
            print(f"Cound not interpret {user_input} as an integer - Please try again")

    raise MaximumQuestionsAnswerWrong(f"Stopped after {n} questions answered wrong",
                                      question_asked=n,
                                      )


def get_floating_point_from_user_input(max_questions: int = _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED) -> Optional[float]:
    """Asks the user for a floating point number.

    Args:
        max_questions (int, optional): Maximum number of wrong answers. Defaults to MAXIMUM_NUMBER_OF_QUESTIONS_ASKED.

    Raises:
        MaximumQuestionsAnswerWrong: If the user does not provide a valid answer too many times.

    Returns:
        Optional[float]: Floating point number that was provided by the user. None is no answer was provided.
    """
    max_questions = min(max_questions, _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED)

    for n in range(1, max_questions+1):
        raw_user_input = input("Please enter a floating-point number: ")

        if not raw_user_input:
            return None
        if not (user_input := raw_user_input.strip()):
            print("Cannot interpret whitespace - Please try again")
            continue
        try:
            return float(user_input)
        except ValueError:
            print(f"Cound not interpret {user_input} as a floating point number - Please try again")
            continue

    raise MaximumQuestionsAnswerWrong(f"Stopped after {n} questions answered wrong",
                                      question_asked=n
                                      )
