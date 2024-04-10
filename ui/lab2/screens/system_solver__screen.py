from customtkinter import *
from typing import *

from util.float_validation import check_input_is_float

from equation.abstraction import SystemTwo

from util.system_math import newton_method_systems

class SystemSolverScreen(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.possible_systems: Dict[str, SystemTwo] = controller.get_all_systems()

    # page title
    label: CTkLabel = CTkLabel(self, text=f'Equation systems', fg_color='transparent')
    label.grid(row=0, pady=10, padx=10, columnspan=2)

    system_variants: List[str] = ['System']
    system_variants.extend(self.possible_systems)
    self.system_choice: CTkComboBox = CTkComboBox(self, values=system_variants, command=lambda c: self.__select_system(c))
    self.system_choice.grid(row=1, padx=10, pady=10, columnspan=2)

    # initial approximation input
    self.input_x0: CTkEntry = CTkEntry(self, placeholder_text='x0:')
    self.input_x0.grid(row=2, column=0, pady=5, padx=4)
    self.input_x0.configure(validate='key', validatecommand=(self.input_x0.register(check_input_is_float), '%P', '%d'))

    self.input_y0: CTkEntry = CTkEntry(self, placeholder_text='y0:')
    self.input_y0.grid(row=2, column=1, pady=5, padx=4)
    self.input_y0.configure(validate='key', validatecommand=(self.input_y0.register(check_input_is_float), '%P', '%d'))

    self.calculate_btn: CTkButton = CTkButton(self, text='Calculate', command=lambda: self.__calculate())
    self.calculate_btn.grid(row=3, pady=10, padx=10, columnspan=2)

    # navigate to start page btn
    nav_back_btn: CTkButton = CTkButton(self, text='Main page', command=lambda: self.controller.show_main_screen())
    nav_back_btn.grid(row=4, pady=10, padx=10, columnspan=2)
  
  def __select_system(self, choice: str):
    if (choice in self.possible_systems.keys()):
      s: SystemTwo = self.possible_systems[choice]
      self.controller.set_system(s)

  def __calculate(self) -> None:
    system: SystemTwo = self.controller.get_system()

    if (system == None):
      self.controller.show_error('System is not selected')
      return

    # validate that initial approximation params are not empty
    x0_str: str = self.input_x0.get()
    if (len(x0_str) < 1):
      self.controller.show_error('x0 approximation cannot be empty')
      return
    y0_str: str = self.input_y0.get()
    if (len(y0_str) < 1):
      self.controller.show_error('y0 approximation cannot be empty')
      return

    x0: float = float(x0_str)
    y0: float = float(y0_str)

    try:
      result: Tuple[float, float, int] = newton_method_systems((x0, y0), system)
      self.controller.show_system_results(-3, 3, system, result)
    except Exception as e:
      self.controller.show_error(e)
