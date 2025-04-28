import numpy as np
import matplotlib.pyplot as plt

from typing import Callable
from numpy.typing import ArrayLike
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from simple.math import identity


def one_dimensional_plot(func: Callable[[ArrayLike], ArrayLike],
                         /,
                         __min: float = 0,
                         __max: float = 1,
                         num: int = 101,
                         xlabel: str = "",
                         ylabel: str = "",
                         title: str = "",
                         grid: bool = False,
                         ) -> tuple[Figure, Axes]:
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    x = np.linspace(__min, __max, num)
    y = func(x)
    ax.plot(x, y)

    ax.grid(grid)
    return fig, ax


def _testplot() -> Figure:
    fig, _ = one_dimensional_plot(identity,
                                  xlabel='x',
                                  ylabel='y',
                                  title='y = x',
                                  grid=True,
                                  )
    return fig


if __name__ == '__main__':
    _testplot()
    plt.show()
