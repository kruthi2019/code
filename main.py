import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt

import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import preprocess as pre
import SVMALG as SVM
import DTALG as DT
#import NeuralNetwork as NN
#import Compare as cc

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def clear():
    print("Clear1")
    txt1.delete(0, 'end')    



window = tk.Tk()
window.title("Breast Cancer Predictions")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Breast Cancer Predictions" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=20)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=100, y=200)

txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=400, y=215)


#lbl4 = tk.Label(window, text="Notification : ",width=20  ,fg=fgcolor,bg=bgcolor  ,height=2 ,font=('times', 15, ' bold underline ')) 
#lbl4.place(x=100, y=400)

#message = tk.Label(window, text="" ,bg="white"  ,fg="black",width=60  ,height=8, activebackground = bgcolor ,font=('times', 15, ' bold ')) 
#message.place(x=400, y=400)

def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	


def preprocess():
	sym=txt.get()
	if sym != "" :
		pre.process(sym)
		print("preprocess")
		tm.showinfo("Input", "Preprocess Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
	
def SVMprocess():
	sym=txt.get()
	if sym != "" :
		SVM.process(sym)
		print("SVM")
		tm.showinfo("Input", "SVM Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
	
def DTprocess():
	sym=txt.get()
	if sym != "" :
		DT.process(sym)
		print("DT")
		tm.showinfo("Input", "DT Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
		
def NNprocess():
	sym=txt.get()
	if sym != "" :
		NN.process(sym)
		print("NN")  
		tm.showinfo("Input", "Neural Network Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
	
def compare():
	sym=txt.get()
	if sym != "" :
		cc.process(sym)
		print("Compare") 
		tm.showinfo("Input", "Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=650, y=200)


clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)
 
process = tk.Button(window, text="Preprocess", command=preprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
process.place(x=10, y=600)

svmbutton = tk.Button(window, text="SVM", command=SVMprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
svmbutton.place(x=210, y=600)

DTreebutton = tk.Button(window, text="Decission Tree", command=DTprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
DTreebutton.place(x=420, y=600)

NNbutton = tk.Button(window, text="Neural Network", command=NNprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
NNbutton.place(x=620, y=600)

cbutton = tk.Button(window, text="Compare", command=compare  ,fg=fgcolor   ,bg=bgcolor1 ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
cbutton.place(x=820, y=600)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1020, y=600)

 
window.mainloop()

