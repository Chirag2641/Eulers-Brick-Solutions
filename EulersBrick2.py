import pyautogui
from time import sleep
import tkinter as tk
import os

a = 1
b = 1
c = 1
x = 0
y = 0
z = 0

def update_values():
    global a,b,c,x,y,z
    while a<100:
        while b<=100:
            while c<=100:
                x=((a**2+b**2)**0.5)
                y=((a**2+c**2)**0.5)
                z=((b**2+c**2)**0.5)
                os.system('clear')
                value_label_a.config(text="a = "+str(a))
                value_label_b.config(text="b = "+str(b))
                value_label_c.config(text="c = "+str(c))
                value_label_x.config(text="x = "+str(x))
                value_label_y.config(text="y = "+str(y))
                value_label_z.config(text="z = "+str(z))
                root.update()
                if (x%1!=0):
                    break
                if (x%1==0) and (y%1==0) and (z%1==0):
                    print("a = " + a)
                    print("b = " + b)
                    print("c = " + c)
                    print("x = " + x)
                    print("y = " + y)
                    print("z = " + z)
                    print("\n")
                c+=1
            b+=1
            c=1
        a+=1
        b=1
    root.after(1000, update_values)

root = tk.Tk()
root.attributes("-topmost", True)
root.geometry("400x300")

value_label_a = tk.Label(root, text="a = ")
value_label_a.pack()
value_label_b = tk.Label(root, text="b = ")
value_label_b.pack()
value_label_c = tk.Label(root, text="c = ")
value_label_c.pack()
value_label_x = tk.Label(root, text="x = ")
value_label_x.pack()
value_label_y = tk.Label(root, text="y = ")
value_label_y.pack()
value_label_z = tk.Label(root, text="z = ")
value_label_z.pack()
update_values()
root.mainloop()
