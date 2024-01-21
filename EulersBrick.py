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

while True:
    while a<500:
        while b<=500:
            while c<=500:
                x=((a**2+b**2)**0.5)
                y=((a**2+c**2)**0.5)
                z=((b**2+c**2)**0.5)
                if (x%1==0) and (y%1==0) and (z%1==0):
                    print("x = " + x)
                    print("y = " + y)
                    print("z = " + z)
                    print("\n")
                c+=1
            b+=1
        a+=1

