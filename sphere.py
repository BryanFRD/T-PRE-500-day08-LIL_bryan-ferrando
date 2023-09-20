from tkinter import *
import math

def create_sphere(canvas, x, y, r):
  n = 50
  for i in range(n):
    angle = 2 * math.pi * i / n
    x1 = x + r * math.cos(angle)
    y1 = y + r * math.sin(angle)
    
    for j in range(n):
      sub_angle = 2 * math.pi * j / n
      x2 = x1 + 20 * math.cos(sub_angle)
      y2 = y1 + 20 * math.sin(sub_angle)
      
      canvas.create_line(x1, y1, x2, y2, fill="blue")
      
root = Tk()
root.title("Sphere")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

x_center = 200
y_center = 200
radius = 100

create_sphere(canvas, x_center, y_center, radius)
root.mainloop()