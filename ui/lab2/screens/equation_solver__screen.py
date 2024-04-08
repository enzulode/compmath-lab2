from customtkinter import *
from typing import *

from equation.abstraction import EquationOne

from ui.lab2.components.empty_form__component import EmptyFormComponent
from ui.lab2.components.bisection_form__component import BisectionFormComponent
from ui.lab2.components.iterative_form__component import IterativeFormComponent
from ui.lab2.components.newton_form__component import NewtonFormComponent

class EquationSolverScreen(CTkFrame):

  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.possible_equations: Dict[str, EquationOne] = controller.get_all_equations()
    
    self.nonbuilt_method_forms: Set[Type] = set([EmptyFormComponent, BisectionFormComponent, IterativeFormComponent, NewtonFormComponent])
    self.built_method_forms: Dict[Type, CTkFrame] = {}

    # page title
    heading: CTkLabel = CTkLabel(self, text='Equations', fg_color='transparent')
    heading.grid(row=0, pady=10, padx=10, columnspan=2)

    # equation selector
    equation_variants: List[str] = ['Equation']
    equation_variants.extend(self.possible_equations)
    self.equation_choice: CTkComboBox = CTkComboBox(self, values=equation_variants, command=lambda c: self.__select_equation(c))
    self.equation_choice.grid(row=1, padx=10, pady=10, columnspan=2)

    # method selector
    method_variants: List[str] = ['Method', 'Bisect', 'Newton', 'Iterative']
    method_choice: CTkComboBox = CTkComboBox(self, values=method_variants, command=lambda c: self.__select_method(c))
    method_choice.grid(row=2, padx=10, pady=10, columnspan=2)

    for MFC in self.nonbuilt_method_forms:
      mfc = MFC(self, controller)
      mfc.grid(row=3, padx=10, pady=10, columnspan=2, sticky='nsew')
      self.built_method_forms[MFC] = mfc
    
    self.show_method_form(EmptyFormComponent)

    # main screen return btn
    nav_back_btn: CTkButton = CTkButton(self, text='Main page', command=lambda: self.controller.show_main_screen())
    nav_back_btn.grid(row=4, pady=10, padx=10, columnspan=2)
  
  def __select_equation(self, choice: str):
    if (choice in self.possible_equations.keys()):
      eq: EquationOne = self.possible_equations[choice]
      self.controller.set_equation(eq)
  
  def show_method_form(self, form_type: Type) -> None:
    if (form_type in self.built_method_forms.keys()):
      self.built_method_forms[form_type].tkraise()

  def __select_method(self, choice: str):
    match choice:
      case 'Bisect': self.show_method_form(BisectionFormComponent)
      case 'Iterative': self.show_method_form(IterativeFormComponent)
      case 'Newton': self.show_method_form(NewtonFormComponent)
      case _: self.show_method_form(EmptyFormComponent)