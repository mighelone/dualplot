from typing import Optional, Union
import matplotlib.pyplot as plt

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

COL_RIGHT = "#C54E6D"
COL_LEFT = "#009380"


class DualPlot:
    """
    Create a plot figure with a dual plot using the style by
    https://www.r-bloggers.com/dual-axes-time-series-plots-may-be-ok-sometimes-after-all/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29
    """

    def __init__(
        self,
        color_left: Optional[str] = None,
        color_right: Optional[str] = None,
        **fig_kw,
    ):
        self._fig, self._axleft = plt.subplots(**fig_kw)
        self._axright = self._axleft.twinx()
        self.col_left = color_left
        self.col_right = color_right

    def _set_ax_properties(self, ax: plt.Axes, side: str) -> None:
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_position(("outward", 20))
        side = side.lower()
        assert side in ("left", "right"), "Only left and right side accepted"
        opp_side = "left" if side == "right" else "right"
        ax.spines[opp_side].set_visible(False)

        color = self.col_right if side == "right" else self.col_left
        ax.spines[side].set_position(("outward", 20))
        ax.spines[side].set_color(color)
        ax.yaxis.set_ticks_position(side)
        ax.xaxis.set_ticks_position("bottom")
        ax.tick_params(axis="y", colors=color)

    def set_xlabel(self, *args, **kwargs) -> None:
        self._axleft.set_xlabel(*args, **kwargs)

    def set_ylabel_left(self, *args, **kwargs) -> None:
        if "color" not in kwargs:
            kwargs["color"] = self._col_left
        self._axleft.set_ylabel(*args, **kwargs)

    def set_ylabel_right(self, *args, **kwargs):
        if "color" not in kwargs:
            kwargs["color"] = self._col_right
        self._axright.set_ylabel(*args, **kwargs)

    def legend(self, *args, **kwargs):
        lines = self._axleft.lines + self._axright.lines
        labels = [l.get_label() for l in lines]
        self._axleft.legend(lines, labels, *args, **kwargs)

    @property
    def col_right(self):
        return self._col_right

    @col_right.setter
    def col_right(self, color: Union[str, None]):
        self._col_right = color if color else COL_RIGHT
        self._set_ax_properties(ax=self.axright, side="right")

    @property
    def col_left(self):
        return self._col_left

    @col_left.setter
    def col_left(self, color: Union[str, None]):
        self._col_left = color if color else COL_LEFT
        self._set_ax_properties(ax=self.axleft, side="left")

    def plot_left(self, *args, **kwargs):
        """Add plot line on the left axis"""
        if "color" not in kwargs:
            kwargs["color"] = self._col_left
        self._axleft.plot(*args, **kwargs)

    def plot_right(self, *args, **kwargs):
        """Add plot line on the right axis"""
        if "color" not in kwargs:
            kwargs["color"] = self._col_right
        self._axright.plot(*args, **kwargs)

    def set_title(self, *args, **kwargs):
        self._axleft.set_title(*args, **kwargs)

    @property
    def axleft(self):
        return self._axleft

    @property
    def axright(self):
        return self._axright

    @property
    def fig(self):
        return self._fig
