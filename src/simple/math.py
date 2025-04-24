"""A library containing the most basic math functions."""
from typing import Literal


def tautology(*_, **__) -> Literal[True]:
    """Returns True no matter what."""
    return True


def contradiction(*_, **__) -> Literal[False]:
    """Returns False no matter what."""
    return False


def identity[T](x: T) -> T:
    """Return back exactly what came in"""
    return x
