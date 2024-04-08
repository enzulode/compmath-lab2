from customtkinter import *
from typing import *

class IterativeFormComponent(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.input_a: CTkEntry = CTkEntry(self, placeholder_text='a:')
    self.input_a.grid(row=0, column=0, pady=5, padx=4)

    self.input_b: CTkEntry = CTkEntry(self, placeholder_text='b:')
    self.input_b.grid(row=0, column=1, pady=5, padx=4)

    self.calculate_btn: CTkButton = CTkButton(self, text='Calculate', command=lambda: self.__calculate())
    self.calculate_btn.grid(row=1, pady=10, padx=10, columnspan=2)
  
  def __calculate(self):
    print('ITERATIVE CALCULATION', self.controller.get_equation())
    # print(basic_iterative_method(float(self.input_a.get()), float(self.input_b.get()), self.selected_equation))
