import pytest

import matplotlib.pyplot as plt
from dualplot import DualPlot

color_left = "red"
color_right = "blue"


@pytest.fixture
def dual_plot():
    return DualPlot(color_left=color_left, color_right=color_right)


def test_init(dual_plot):
    assert dual_plot.col_left == color_left
    assert dual_plot.col_right == color_right

    assert isinstance(dual_plot._fig, plt.Figure)
    assert isinstance(dual_plot._axright, plt.Axes)
    assert isinstance(dual_plot._axleft, plt.Axes)


def test_set_ax_properties(dual_plot):
    ax = dual_plot._axleft
    dual_plot._set_ax_properties(ax=ax, side="left")

    assert ax.spines["top"].properties()["visible"] == False
    assert ax.spines["bottom"].properties()["position"] == ("outward", 20)

    assert ax.spines["left"].properties()["position"] == ("outward", 20)
    # assert ax.spines["left"].properties()["color"] == dual_plot.col_left
    assert ax.spines["right"].properties()["visible"] == False
