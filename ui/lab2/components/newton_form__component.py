from customtkinter import *
from typing import *

class NewtonFormComponent(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.input_x0: CTkEntry = CTkEntry(self, placeholder_text='x0:')
    self.input_x0.grid(row=0, pady=10, padx=10, columnspan=2)

    self.calculate_btn: CTkButton = CTkButton(self, text='Calculate', command=lambda: self.__calculate())
    self.calculate_btn.grid(row=1, pady=10, padx=10, columnspan=2)
  
  def __calculate(self):
    print('NEWTON CALCULATION', self.controller.get_equation())
    # print(newton_method(float(self.input_x0.get()), self.selected_equation))
