import pytest

from dualplot import DualPlot

color_left = "red"
color_right = "blue"


@pytest.fixture
def dual_plot():
    return DualPlot(color_left=color_left, color_right=color_right)


def test_init(dual_plot):
    assert dual_plot.col_left == color_left
    assert dual_plot.col_right == color_right
