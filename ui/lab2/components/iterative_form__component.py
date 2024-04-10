from customtkinter import *
from typing import *

from equation.abstraction import EquationOne

from util.equation_math import basic_iterative_method

from util.float_validation import check_input_is_float

class IterativeFormComponent(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.input_a: CTkEntry = CTkEntry(self, placeholder_text='a:')
    self.input_a.grid(row=0, column=0, pady=5, padx=4)
    self.input_a.configure(validate='key', validatecommand=(self.input_a.register(check_input_is_float), '%P', '%d'))

    self.input_b: CTkEntry = CTkEntry(self, placeholder_text='b:')
    self.input_b.grid(row=0, column=1, pady=5, padx=4)
    self.input_b.configure(validate='key', validatecommand=(self.input_a.register(check_input_is_float), '%P', '%d'))

    self.calculate_btn: CTkButton = CTkButton(self, text='Calculate', command=lambda: self.__calculate())
    self.calculate_btn.grid(row=1, pady=10, padx=10, columnspan=2)
  
  def __calculate(self):
    eq: EquationOne = self.controller.get_equation()

    if (eq == None):
      self.controller.show_error('Equation is not selected')
      return

    # validate that interval params are not empty
    a_str: str = self.input_a.get()
    if (len(a_str) < 1):
      self.controller.show_error('Left interval border cannot be empty')
      return
    b_str: str = self.input_b.get()
    if (len(b_str) < 1):
      self.controller.show_error('Right interval border cannot be empty')
      return

    a: float = float(a_str)
    b: float = float(b_str)

    try:
      result: Tuple[float, int] = basic_iterative_method(a, b, eq)
      self.controller.show_equation_results(-3, 3, eq, result)
    except Exception as e:
      self.controller.show_error(e)
