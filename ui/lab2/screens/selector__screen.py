from customtkinter import *
from typing import *

from ui.lab2.screens.equation_solver__screen import EquationSolverScreen
from ui.lab2.screens.system_solver__screen import SystemSolverScreen

class SolverSelectorScreen(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller

    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)
    self.__font = CTkFont('Poppins', 20, 'bold')

    title: CTkLabel = CTkLabel(self, text='Mode selection', fg_color='transparent', font=self.__font)
    title.grid(row=0, padx=10, pady=10, columnspan=2)
  
    nav_btn1: CTkButton = CTkButton(self, text='Equations', command=lambda: self.controller.show_screen(EquationSolverScreen))
    nav_btn1.grid(row=1, padx=10, pady=10, columnspan=2)

    nav_btn2: CTkButton = CTkButton(self, text='Equation systems', command=lambda: self.controller.show_screen(SystemSolverScreen))
    nav_btn2.grid(row=2, padx=10, pady=10, columnspan=2)