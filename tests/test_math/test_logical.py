"""Test logical function from the simple.math module."""
import pytest
from simple.math import tautology, contradiction


ARBITARY_TYPE_MOCK_INPUTS = [1, '3', (1, 2), object(), int]
ARBITARY_TYPE_MOCK_MANY_INPUT_DICT = [
    {'a': 1},
    {'a': 1, 'b': int},
    {'a': 1, 'z': (1, 2, 3)},
]


def test_tautology_trivial() -> None:
    assert tautology()


@pytest.mark.parametrize('__input', ARBITARY_TYPE_MOCK_INPUTS)
def test_tautology_single(__input) -> None:
    assert tautology(__input)


def test_tautology_many() -> None:
    assert tautology(*ARBITARY_TYPE_MOCK_INPUTS)


@pytest.mark.parametrize('kwargs', ARBITARY_TYPE_MOCK_MANY_INPUT_DICT)
def test_tautology_keywords(kwargs) -> None:
    assert tautology(**kwargs)


def test_contradiction_trivial() -> None:
    assert not contradiction()


@pytest.mark.parametrize('__input', ARBITARY_TYPE_MOCK_INPUTS)
def test_contradiction_single(__input) -> None:
    assert not contradiction(__input)


def test_contradiction_many() -> None:
    assert not contradiction(*ARBITARY_TYPE_MOCK_INPUTS)


@pytest.mark.parametrize('kwargs', ARBITARY_TYPE_MOCK_MANY_INPUT_DICT)
def test_contradiction_many_keywords(kwargs) -> None:
    assert not contradiction(**kwargs)
