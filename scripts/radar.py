# code for creating the 'radar' plot showing quantification features of quantification methods
# adapted from source: http://matplotlib.org/xkcd/examples/api/radar_chart.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection

def _radar_factory(num_vars):
    theta = 2*np.pi * np.linspace(0, 1-1./num_vars, num_vars)
    theta += np.pi/2

    def unit_poly_verts(theta):
        x0, y0, r = [0.5] * 3
        verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
        return verts

    class RadarAxes(PolarAxes):
        name = 'radar'
        RESOLUTION = 1

        def fill(self, *args, **kwargs):
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(theta * 180/np.pi, labels)

        def _gen_axes_patch(self):
            verts = unit_poly_verts(theta)
            return plt.Polygon(verts, closed=True, edgecolor='k')

        def _gen_axes_spines(self):
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            verts.append(verts[0])
            path = Path(verts)
            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta

def radar_graph(labels, names, colors, *lists):
    N = len(labels)
    theta = _radar_factory(N)
    max_val = max(map(max,lists))
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(1, 1, 1, projection='radar')
    styles = ('-','--','-','--')
    for list,color,style in zip(lists,colors,styles):
        ax.plot(theta, list, color=color, linewidth=5, zorder=-10, linestyle=style)
        ax.fill(theta, list, facecolor=color, alpha=0.1)
    ax.set_varlabels(labels)
    ax.set_yticks([])
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize('large')
    legend = ax.legend(names, loc=(-0.4, .8),labelspacing=0.1, fontsize='large')
    plt.show()
    #plt.savefig("radar.png", dpi=100)
