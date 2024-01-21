import pyautogui
from time import sleep
import tkinter as tk
import os
import threading

min = 500000005000
a = min
b = min
c = min
x = 0
y = 0
z = 0
q = 0
iter = 5000
solutions = 0

def update_values():
    global a,b,c,x,y,z,q,solutions
    while a<=min+iter:
        while b<=min+iter:
            while c<=min+iter:
                x=((a**2+b**2)**0.5)
                y=((a**2+c**2)**0.5)
                z=((b**2+c**2)**0.5)
                q=((a**2+b**2+c**2)**0.5)
                if (x%1!=0):
                    break
                if (x%1==0) and (y%1==0) and (z%1==0) and (q%1==0):
                    solutions+=1
                    with open('perfectSolutions.txt', 'a') as f:   
                        f.write("Solution No.: " + str(solutions) + "\n") 
                        f.write("a = " + str(a) + "\n")
                        f.write("b = " + str(b) + "\n")
                        f.write("c = " + str(c) + "\n")
                        f.write("x = " + str(x) + "\n")
                        f.write("y = " + str(y) + "\n")
                        f.write("z = " + str(z) + "\n")
                        f.write("\n")
                    
                c+=min
            b+=1
            c=min
        a+=1
        b=min


   
def update_labels():
    while True:
        value_label_a.config(text="a = "+str(a))
        value_label_b.config(text="b = "+str(b))
        value_label_c.config(text="c = "+str(c))
        value_label_x.config(text="x = "+str(x))
        value_label_y.config(text="y = "+str(y))
        value_label_z.config(text="z = "+str(z))
        value_label_q.config(text="q = "+str(q))
        root.update()
        
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
value_label_q = tk.Label(root, text="q = ")
value_label_q.pack()

thread1 = threading.Thread(target=update_values)
thread2 = threading.Thread(target=update_labels)

thread1.start()
thread2.start()
root.mainloop()

min = min+iter