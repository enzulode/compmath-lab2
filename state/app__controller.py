from customtkinter import *
from typing import *

from equation.abstraction import EquationOne
from equation.first_equation import FirstEquation
from equation.second_equation import SecondEquation
from equation.third_equation import ThirdEquation

from equation.abstraction import EquationTwo
from equation.abstraction import SystemTwo
from equation.first_system import FirstSystem
from equation.second_system import SecondSystem

from ui.lab2.screens.selector__screen import SolverSelectorScreen
from ui.lab2.screens.equation_solver__screen import EquationSolverScreen
from ui.lab2.screens.system_solver__screen import SystemSolverScreen

from ui.lab2.windows.dialog_window__window import DialogWindow

import matplotlib.pyplot as plt
import numpy as np

class ApplicationController(CTk):

  def __init__(self):
    super().__init__()
    self.geometry('600x500')
    self.title('LAB: comp-math')

    # Equation management stuff
    self.equation_types: List[Type] = [FirstEquation, SecondEquation, ThirdEquation]
    self.equations: Dict[str, EquationOne] = {}
    for E in self.equation_types:
      eq = E()
      self.equations[str(eq)] = eq
    self.current_equation: EquationOne = None

    # Systems management stuff
    self.system_types: List[Type] = [FirstSystem, SecondSystem]
    self.systems: Dict[str, SystemTwo] = {}
    for S in self.system_types:
      system = S()
      self.systems[str(system)] = system
    self.current_system: SystemTwo = None

    self.nonbuilt_screens: Set[Type] = set([SolverSelectorScreen, EquationSolverScreen, SystemSolverScreen])
    self.built_screens: Dict[Type, CTkFrame] = {}

    # Init ui holder container
    self.container: CTkFrame = CTkFrame(self)
    self.container.pack(side='top', fill='both', expand=True)
    self.container.grid_rowconfigure(0, weight=1)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Build all available screens
    for P in self.nonbuilt_screens:
      screen = P(self.container, self)
      screen.grid(row=0, column=0, sticky='nsew')
      self.built_screens[P] = screen

    self.show_screen(SolverSelectorScreen)

  def set_equation(self, eq: EquationOne) -> None:
    self.current_equation = eq

  def get_equation(self) -> EquationOne:
    return self.current_equation
  
  def get_all_equations(self) -> Dict[str, EquationOne]:
    return self.equations
  
  def set_system(self, s: SystemTwo) -> None:
    self.current_system = s

  def get_system(self) -> SystemTwo:
    return self.current_system
  
  def get_all_systems(self) -> Dict[str, SystemTwo]:
    return self.systems
  
  def show_screen(self, page_type: Type) -> None:
    if (page_type in self.built_screens.keys()):
      self.built_screens[page_type].tkraise()

  def show_main_screen(self) -> None:
    self.show_screen(SolverSelectorScreen)
  
  def show_dialog_window(self, title: str, message: str) -> None:
    error_window: DialogWindow = DialogWindow(title, message)
    error_window.mainloop()
  
  def draw_graph_equation(self, a: float, b: float, eq: EquationOne, solution: float) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    x = np.arange(a, b, 0.001)
    y = [eq.func(v) for v in x]
    ax.plot(x, y)

    ax.set_xticks(np.arange(a, b, 0.5))
    ax.set_yticks(np.arange(a, b, 0.5))
    ax.set_xlim(a, b)
    ax.set_ylim(a, b)

    ax.scatter([solution], [0], color='red')

    plt.show()  

  def draw_graph_system(self, a: float, b: float, solution: Tuple[float, float], system: SystemTwo) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    space = np.arange(a, b, 0.001)
    f1 = [system.get_equation1().func_sided(f1_arg, f1_arg) for f1_arg in space]
    ax.plot(space, f1, color='red')

    f2 = [system.get_equation2().func_sided(f2_arg, f2_arg) for f2_arg in space]
    ax.plot(f2, space, color='blue')

    ax.scatter([solution[0]], [solution[1]], color='black')
    
    plt.show()