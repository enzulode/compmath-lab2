from customtkinter import *
from typing import *

class DialogWindow(CTk):
  
  def __init__(self, window_title: str, error_text: str):
    super().__init__()
    self.geometry('600x200')
    self.title(window_title)

    label: CTkLabel = CTkLabel(self, text=error_text, height=40, wraplength=500)
    label.pack(expand=True)
    