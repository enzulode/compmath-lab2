from customtkinter import *
from typing import *

class SystemSolverScreen(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    label: CTkLabel = CTkLabel(self, text='Equation systems', fg_color='transparent')
    label.grid(row=0, pady=10, padx=10, columnspan=2)

    # navigate to start page btn
    nav_back_btn: CTkButton = CTkButton(self, text='Main page', command=lambda: self.controller.show_main_screen())
    nav_back_btn.grid(row=1, pady=10, padx=10, columnspan=2)
