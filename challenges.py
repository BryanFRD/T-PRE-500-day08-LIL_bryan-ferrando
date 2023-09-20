from tkinter import *
from game.Main import Main

root = Tk()
root.title("Game")
root.geometry("400x400")

game = Main(root)

root.mainloop()