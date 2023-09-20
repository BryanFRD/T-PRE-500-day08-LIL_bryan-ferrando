from tkinter import *

class Game(Frame):
  
  def __init__(self, parent):
    super().__init__(parent)
    text = Text(self, "test")
    text.grid()