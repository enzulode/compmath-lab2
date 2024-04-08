from customtkinter import *
from typing import *

from equation.abstraction import EquationOne
from equation.first_equation import FirstEquation
from equation.second_equation import SecondEquation
from equation.third_equation import ThirdEquation

from ui.lab2.screens.selector__screen import SolverSelectorScreen
from ui.lab2.screens.equation_solver__screen import EquationSolverScreen
from ui.lab2.screens.system_solver__screen import SystemSolverScreen

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
  
  def show_screen(self, page_type: Type) -> None:
    if (page_type in self.built_screens.keys()):
      self.built_screens[page_type].tkraise()

  def show_main_screen(self) -> None:
    self.show_screen(SolverSelectorScreen)
  
