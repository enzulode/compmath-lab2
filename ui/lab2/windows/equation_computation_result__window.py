from customtkinter import *
from typing import *

from equation.abstraction import EquationOne

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure, Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EquationComputationResultWindow(CTkToplevel):
  def __init__(self, message: str, interval: Tuple[float, float], eq: EquationOne, results: Tuple[float, int], *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

    self.title('Computation result')
    self.geometry('600x600')

    # window message
    label: CTkLabel = CTkLabel(self, text=message, height=40, wraplength=500)

    # create figure for the plot
    fig: Figure = plt.figure(figsize=(5,5), dpi=100)
    ax: Axes = fig.add_subplot(1, 1, 1)

    # configure spines
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # configure axes ticks
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(interval[0], interval[1], 0.5))
    ax.set_yticks(np.arange(interval[0], interval[1], 0.5))
    ax.set_xlim(interval[0], interval[1])
    ax.set_ylim(interval[0], interval[1])

    # draw desired plot
    x = np.arange(interval[0], interval[1], 0.001)
    y = [eq.func(v) for v in x]
    ax.plot(x, y)
    ax.scatter([results[0]], [0], color='red')

    # init canvas with plot and fill the plot into canvas
    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(figure=fig, master=self)
    canvas.draw()

    # pack computation result message and plot canvas on the screen 
    label.pack()
    canvas.get_tk_widget().pack()
