from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import math

GUI = Tk()
GUI.title ('โปรแกรมคำนวณกระแสจาก Rectifier')
GUI.geometry("400x300")

L1 = Label(GUI ,text = 'ใส่ขนาด Rectifier :',font = ('Angsana New',15),fg = 'black')
L1.place (x=20 , y=30)
L2 = Label(GUI,text = 'ใส่จำนวน Rectifier :',font = ('Angsana New',15),fg = 'black')
L2.place (x=20 , y=60)
L3 = Label(GUI,text = 'ใส่จำนวนแรงดัน DC :',font = ('Angsana New',15),fg = 'black')
L3.place (x=20 , y=90)
L4 = Label(GUI,text = 'กระแส MAX :',font = ('Angsana New',15),fg = 'black')
L4.place (x=20 , y=150)
L5 = Label(GUI,text = 'วัตต์',font = ('Angsana New',15),fg = 'black')
L5.place (x=300, y=30)
L6 = Label(GUI,text = 'ตัว',font = ('Angsana New',15),fg = 'black')
L6.place (x=300 , y=60)
L6 = Label(GUI,text = 'โวลต์',font = ('Angsana New',15),fg = 'black')
L6.place (x=300 , y=90)
L7 = Label(GUI,text = 'แอมป์',font = ('Angsana New',15),fg = 'black')
L7.place (x=300 , y=150)
def button_click():
    value = input1.get()
    a = int(value)
    value2 = input2.get()
    b = int (value2)
    value3 = input3.get()
    c = int (value3)
    value4 = (a*b)//c
    input4.delete(0, tk.END)
    input4.insert(0, value4)
    


input1 = tk.Entry(GUI, bg='cyan',fg='black')
input1.place(x=150,y=40)
input2 = tk.Entry(GUI, bg='cyan',fg='black')
input2.place(x=150,y=70)
input3 = tk.Entry(GUI, bg='cyan',fg='black')
input3.place(x=150,y=100)
input4 = tk.Entry(GUI, bg='lightgreen',fg='black')
input4.place(x=150,y=160)

button = ttk.Button(GUI,text='คำนวณกระแส', command=button_click)
button.place(x=150, y= 200)

GUI.mainloop()



