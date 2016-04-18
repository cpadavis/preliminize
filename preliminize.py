"""
A license should go here.
"""

import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from math import pi, atan2, sqrt

def preliminize(text="Preliminary", ax=None, **kwargs):
    """A very simple code for adding words to a figure.

    Parameters
    ----------

    text : str, default "Preliminary"
        Text we add to figure.

    location : list of coordinates
        From where to where do we want the text to span?

    ax : matplotlib axis
        What axis?

    kwargs : goes into the text

    Returns
    -------

    axis that is preliminized
    """

    # get axis if no ax is provided
    if not ax:
        ax = plt.gca()
    fontdict = {'horizontalalignment': 'center',
                'verticalalignment': 'center',
                'fontname': 'Arial',
                'alpha': 0.2}

    # get rotation from axis to display
    x0, y0 = ax.transAxes.transform((0, 0))
    x1, y1 = ax.transAxes.transform((1, 1))
    dy = y0 - y1
    dx = x1 - x0
    rotation = 180 / pi * atan2(dy, dx)

    # get fontsize from display extent
    bb0 = TextPath((0, 0), text, size=50, props=fontdict).get_extents()
    bb1 = TextPath((0, 0), text, size=51, props=fontdict).get_extents()
    dw = bb1.width - bb0.width  # display / size
    dh = bb1.height - bb0.height  # display / size
    # get the hypotenuse: through a little math in the display system, we
    # realize that hypot = h tan theta + w, where h and w are the height and
    # width of the text tan theta = dy / dx from earlier. we multiply by 0.75
    # because this didn't actually work perfectly.
    size = int(sqrt(dy ** 2 + dx ** 2) / (dh * abs(dy / dx) + dw) * 0.75)
    fontdict['size'] = size

    # update with any kwargs
    fontdict.update(kwargs)

    # set the text
    ax.text(0.5, 0.5, text, fontdict=fontdict, rotation=rotation, transform=ax.transAxes)



if __name__ == "__main__":
    # test case
    fig, ax = plt.subplots(figsize=(8, 6))
    x = range(10)
    y = [xi ** 2 + 1 for xi in x]
    ax.plot(x, y)

    preliminize()
    plt.savefig('preliminize.png')
