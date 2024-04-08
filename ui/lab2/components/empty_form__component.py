from customtkinter import *
from typing import *

class EmptyFormComponent(CTkFrame):
  def __init__(self, parent: CTkFrame, controller):
    CTkFrame.__init__(self, parent)
    self.parent: CTkFrame = parent
    self.controller = controller
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    label: CTkLabel = CTkLabel(self, text='You have to choose a method', fg_color='transparent')
    label.grid(row=0, padx=10, pady=10, columnspan=2)
