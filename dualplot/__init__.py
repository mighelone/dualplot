from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import matplotlib.pyplot as plt

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

COL_RIGHT = "#C54E6D"
COL_LEFT = "#009380"


class DualPlot(object):
    '''
    Create a plot figure with a dual plot using the style by 
    https://www.r-bloggers.com/dual-axes-time-series-plots-may-be-ok-sometimes-after-all/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29
    '''

    def __init__(self, color_left=None, color_right=None, **fig_kw):
        self._fig, self._axleft = plt.subplots(**fig_kw)
        self._axright = self._axleft.twinx()
        self.col_left = color_left
        self.col_right = color_right

    def _set_axleft(self):
        '''
        Set the left axis
        '''
        ax = self._axleft
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_position(('outward', 20))
        ax.spines['left'].set_position(('outward', 20))
        ax.spines['left'].set_color(self._col_left)
        ax.spines['left'].set_color(self._col_left)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        ax.tick_params(axis='y', colors=self._col_left)
        # ax.set_ylabel('Sigmoid, m', color=self._col_left)

    def _set_axright(self):
        '''
        Set the right axis
        '''
        ax1 = self._axright
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        ax1.spines['bottom'].set_position(('outward', 20))
        ax1.spines['right'].set_position(('outward', 20))
        ax1.spines['right'].set_color(self._col_right)

        ax1.tick_params(axis='y', colors=self._col_right)
        # ax1.set_ylabel('Other scale', color=self._col_right)
        ax1.grid('off')

    def set_xlabel(self, *args, **kwargs):
        self._axleft.set_xlabel(*args, **kwargs)

    def set_ylabel_left(self, *args, **kwargs):
        if 'color' not in kwargs:
            kwargs['color'] = self._col_left
        self._axleft.set_ylabel(*args, **kwargs)

    def set_ylabel_right(self, *args, **kwargs):
        if 'color' not in kwargs:
            kwargs['color'] = self._col_right
        self._axright.set_ylabel(*args, **kwargs)

    def legend(self, *args, **kwargs):
        lines = self._axright.lines + self._axleft.lines
        labels = [l.get_label() for l in lines]
        self._axleft.legend(lines, labels, *args, **kwargs)

    @property
    def col_right(self):
        return self._col_right

    @col_right.setter
    def col_right(self, color):
        if color is None:
            color = COL_RIGHT
        self._col_right = color
        self._set_axright()

    @property
    def col_left(self):
        return self._col_left

    @col_left.setter
    def col_left(self, color):
        if color is None:
            color = COL_LEFT
        self._col_left = color
        self._set_axleft()

    def plot_left(self, *args, **kwargs):
        '''Add plot line on the left axis'''
        if 'color' not in kwargs:
            kwargs['color'] = self._col_left
        self._axleft.plot(*args, **kwargs)

    def plot_right(self, *args, **kwargs):
        '''Add plot line on the right axis'''
        if 'color' not in kwargs:
            kwargs['color'] = self._col_right
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
