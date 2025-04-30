"""
Test if the get user input works
"""
import pytest
from typing import Callable, Any

from simple.io import (get_integer_from_user_input,
                       MaximumQuestionsAnswerWrong,
                       _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED,
                       )


VALID_INPUT_STRINGS_PAIRS = [
    ('130', 130),
    ('  31231 ', 31231),
    ('+0', 0),
    ('-0', 0),
    ('+1012', 1012),
    ('  -13120', -13120),
]


INVALID_INPUT_STRINGS = [
    'sjdaskld',
    '1012+',
    '++1',
    '+',
    '-',
    'jjr#101',
    '1.0',
]


def _create_mock_input(string: str) -> Callable[[Any], str]:
    def mockinput(*_) -> str:
        return string
    return mockinput


def test_no_answer(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', _create_mock_input(''))
    assert get_integer_from_user_input() is None


def test_whitespace_answer(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', _create_mock_input('     '))
    with pytest.raises(MaximumQuestionsAnswerWrong):
        get_integer_from_user_input(max_questions=1)


@pytest.mark.parametrize(['string', 'expected'], VALID_INPUT_STRINGS_PAIRS)
def test_valid(string: str, expected: int, monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", _create_mock_input(string))
    assert expected == get_integer_from_user_input()


@pytest.mark.parametrize('string', INVALID_INPUT_STRINGS)
def test_invalid(string: str, monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', _create_mock_input(string))

    with pytest.raises(MaximumQuestionsAnswerWrong):
        get_integer_from_user_input()


@pytest.mark.parametrize('max_questions', [1, 2, 10])
def test_max_question_variable(max_questions: int, monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', _create_mock_input('aaa'))
    try:
        get_integer_from_user_input(max_questions=max_questions)
    except MaximumQuestionsAnswerWrong as err:
        assert err.question_asked == max_questions
    else:
        assert False, "Did not raise a MaximumQuestionsAnswerWrong exception"


def test_snaps_maximum_number_of_max_default(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', _create_mock_input('aaa'))
    try:
        get_integer_from_user_input(max_questions=10_000)
    except MaximumQuestionsAnswerWrong as err:
        assert err.question_asked == _MAXIMUM_NUMBER_OF_QUESTIONS_ASKED
    else:
        assert False, "Did not raise a MaximumQuestionsAnswerWrong exception"
