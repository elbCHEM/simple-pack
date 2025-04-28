"""A library containing the most basic math functions."""
import warnings
from typing import Literal, Callable, Hashable, Any


class FloatingPointPrecissionWarning(UserWarning):
    pass


def tautology(*_, **__) -> Literal[True]:
    """Returns True no matter what."""
    return True


def contradiction(*_, **__) -> Literal[False]:
    """Returns False no matter what."""
    return False


def identity[T](x: T) -> T:
    """Return back exactly what came in"""
    return x


def constant_func[T](constant: T) -> Callable[[Any], T]:
    """Generate a function that returns the same value no matter the input"""
    def func(*_, **__) -> T:
        return constant
    return func


def onefunc() -> Callable[[Any], Literal[1]]:
    """Return a function that always returns 1"""
    return constant_func(1)


def zerofunc() -> Callable[[Any], Literal[0]]:
    """Return a function that always returns 0"""
    return constant_func(0)


def invert_dict[Input:Hashable, Output:Hashable](__map: dict[Input, Output],
                                                 /,
                                                 supress_warning: bool = False,
                                                 ) -> dict[Output, Input]:
    """Invert a unique map so that keys and values exchange places.

    A unique map is defined such that no two keys have the same value.


    Raises:
        ValueError: If two keys have the same value.
        FloatingPointPrecissionWarning

    Returns:
        dict[Output, Input]: Invertable map
    """
    if any(isinstance(val, float) for val in __map.values()) and not supress_warning:
        warnings.warn('Dictionary has floating point values - Cannot determine if map is unique',
                      FloatingPointPrecissionWarning
                      )

    inverse_map = {}
    for key, value in __map.items():
        if value in inverse_map:
            raise ValueError('Map does not describe a unique mapping.')
        inverse_map[value] = key

    return inverse_map
