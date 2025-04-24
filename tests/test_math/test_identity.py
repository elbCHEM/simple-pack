"""Test the identity function from the simple.math module"""
import pytest
from simple.math import identity


MUTABLE_TYPE_EXAMPLES = [[1, 2], {1, 2}, {'a': 1, 'b': 2}]
IMMUTABLE_TYPE_EXAMPLES = [1, 2.0, "hello", (1, 2, 3)]


@pytest.mark.parametrize("__input", MUTABLE_TYPE_EXAMPLES)
def test_with_mutable_input(__input) -> None:
    assert __input is identity(__input)


@pytest.mark.parametrize("__input", IMMUTABLE_TYPE_EXAMPLES)
def test_with_immutable_input(__input) -> None:
    assert __input is identity(__input)
