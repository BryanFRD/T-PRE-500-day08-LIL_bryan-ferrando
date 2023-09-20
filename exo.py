import numpy as np
from matplotlib import pyplot as plt
import math

def display_graph(args):
  x, y, = [], []
  for xx, yy in args:
    x += [xx]
    y += [yy]
  
  plt.plot(x, y, 'o', color='red')
  plt.grid()
  plt.show()


#display_graph([(0, 12), (1, 32), (2, 42), (3, 52)])

def f(x):
  return x**2 + x*3 + 2

def plot_fct(f, x, y):
  plt.plot([f(i) for i in range(x, y)])
  plt.grid()
  plt.show()

#plot_fct(math.sin, 0, 50)
#plot_fct(f, -100, 200)
#plot_fct(lambda x: x**2, -10, 10)
#plot_fct(lambda x: 1/x if not x == 0 else 0, -100, 100)

from tkinter import *
import time

def t1():
  root = Tk()
  root.geometry("400x400")
  canvas = Canvas(bg="white")
  canvas.pack(fill=BOTH, expand=YES)
  image = PhotoImage(file="bg.png")
  canvas.create_image(0, 0, image=image, anchor=NW)
  canvas.create_window(100, 10, anchor=NW)
  frame = LabelFrame(root, text="This is a test")
  canvas.create_window(125, 150, anchor=NW, window=frame)
  entry = Entry(frame)
  entry.pack()
  button = Button(frame, text="Write in console", command=lambda: print(f"Input text: {entry.get().upper()}"))
  button.pack()

  root.mainloop()
  
t1()

root = Tk()
root.geometry("500x600")

canvas = Canvas(bg="white")
canvas.pack(fill=BOTH, expand=YES)

canvas.create_oval(200, 50, 300, 150, fill="lime")
la = canvas.create_line(125, 200, 250, 175, width=20, fill="red")
ra = canvas.create_line(250, 175, 375, 200, width=20, fill="blue")
canvas.create_line(125, 425, 250, 340, width=20, fill="purple")
canvas.create_line(250, 340, 375, 425, width=20, fill="orange")
canvas.create_line(250, 150, 250, 355, width=20, fill="green")

def animate(la, ra, i = 0):
  lc = canvas.coords(la)
  rc = canvas.coords(ra)
  
  canvas.delete(la, ra)
  la = canvas.create_line(lc[0], lc[1] + math.sin(i)*10, lc[2], lc[3], width=20, fill="red")
  ra = canvas.create_line(rc[0], rc[1], rc[2], rc[3] + math.sin(i)*10, width=20, fill="blue")
  
  i+=1
  
  root.update()
  root.after(100, animate, la, ra, i)

root.after(100, animate, la, ra)
root.mainloop()