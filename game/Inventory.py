from tkinter import *

class Inventory(Frame):
  
  label: Label = None
  text: Entry = None
  
  def __init__(self, parent):
    super().__init__(parent)
    self.label = Label(self, text="Item: ")
    self.label.grid(column=0, row=0)
    self.text = Entry(self)
    self.text.grid(column=1, row=0)
    inventory_button = Button(self, text="Add", command=self.add_item)
    inventory_button.grid(column=2, row=0)
    self.grid()
    
  def add_item(self):
    f = Frame(self)
    l = Label(f, text=self.text.get())
    l.grid(column=0, row=0)
    b = Button(f, text="X", command=lambda : f.destroy())
    b.grid(column=1, row=0)
    f.grid()
    return