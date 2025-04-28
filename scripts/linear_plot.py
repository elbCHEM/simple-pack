import simple.plot
import matplotlib as plt


def f(x):
    return x*x


fig, _ = simple.plot.one_dimensional_plot(f)
plt.show()
