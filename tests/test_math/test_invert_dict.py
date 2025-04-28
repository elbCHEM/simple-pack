import pytest
from typing import Any
from simple.math import invert_dict, FloatingPointPrecissionWarning


UNIQUE_DICTS = [
    {'a': 1, 'b': 2, 'c': 10},
    {'a': 1, 'b': 2, 'c': (1, 2, 3)},
]


NON_HASHABLE_VALUES = [
    {'a': [1, 2], 'b': "fafa", 'c': 11},
    {'a': 5, 'b': {'a': 123}, 'c': 11},
]


NON_UNIQUE_VALUES = [
    {'a': 10, 'b': 10},
    {'a': 10, 'b': 1, 'c': "ad", 'd': 1},
]


INCLUDES_FLOATS = [
    {'A': 1.0, 'B': 123.0},
    {'A': 1.0, 'B': "DSAD"},
]


def test_empty_dict() -> None:
    assert not invert_dict({})


@pytest.mark.parametrize('__dict', UNIQUE_DICTS)
def test_invertion(__dict: dict) -> None:
    __iverse_dict = invert_dict(__dict)

    for key, value in __dict.items():
        assert __iverse_dict[value] == key
    for key, value in __iverse_dict.items():
        assert __dict[value] == key


@pytest.mark.parametrize('__dict', NON_HASHABLE_VALUES)
def test_non_hashable(__dict: dict) -> None:
    with pytest.raises(TypeError):
        invert_dict(__dict)


@pytest.mark.parametrize('__dict', NON_UNIQUE_VALUES)
def test_non_unique(__dict: dict) -> None:
    with pytest.raises(ValueError):
        invert_dict(__dict)


@pytest.mark.parametrize('__dict', INCLUDES_FLOATS)
def test_floating_point_warning(__dict: dict[Any, float|Any]) -> None:
    with pytest.warns(FloatingPointPrecissionWarning):
        invert_dict(__dict)


@pytest.mark.filterwarnings('error')
@pytest.mark.parametrize('__dict', INCLUDES_FLOATS)
def test_no_warning(__dict: dict[Any, float|Any]) -> None:
    if not any(isinstance(x, float) for x in __dict.values()):
        raise Exception('Invalid test')

    try:
        invert_dict(__dict, supress_warning=True)
    except Exception:
        assert False, "Warning was not supressed"
