from tkinter import *
from Game import Game
from Inventory import Inventory

class Main(Frame):
  
  game: Game = None
  inventory: Inventory = None
  
  def __init__(self, parent):
    super().__init__(parent)
    self.game = Game(parent)
    self.inventory = Inventory(parent)
    self.inventory.grid(column=0, row=0)