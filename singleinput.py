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
import pandas as pd

#import predict as pred
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

import preprocess as pre
import train as tr


bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"


def clear():
    print("Clear1")
    txt1.delete(0, 'end')    
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')
    txt4.delete(0, 'end')   
    txt5.delete(0, 'end')   
    txt6.delete(0, 'end')   
    txt7.delete(0, 'end')   
    txt8.delete(0, 'end')   
    txt9.delete(0, 'end')   
    txt10.delete(0, 'end')   



window = tk.Tk()
window.title("Breast Cancer Predictions")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Breast Cancer Predictions" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=20)

lbl1 = tk.Label(window, text="Clump Thickness",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=50, y=200)

txt1 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt1.place(x=300, y=200)

lbl2 = tk.Label(window, text="Uniformity of Cell Size",width=20  ,fg=fgcolor  ,bg=bgcolor    ,height=1 ,font=('times', 15, ' bold ')) 
lbl2.place(x=50, y=250)

txt2 = tk.Entry(window,width=15 ,fg=fgcolor,font=('times', 15, ' bold ')  )
txt2.place(x=300, y=250)

lbl3 = tk.Label(window, text="Uniformity of Cell Shape",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl3.place(x=50, y=300)

txt3 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt3.place(x=300, y=300)

lbl4 = tk.Label(window, text="Marginal Adhesion ",width=20  ,fg=fgcolor  ,bg=bgcolor   ,height=1 ,font=('times', 15, ' bold ')) 
lbl4.place(x=50, y=350)

txt4 = tk.Entry(window,width=15  ,fg=fgcolor,font=('times', 15, ' bold ')  )
txt4.place(x=300, y=350)

lbl5 = tk.Label(window, text="Single Epithelial Cell Size",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl5.place(x=50, y=400)

txt5 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt5.place(x=300, y=400)

lbl6 = tk.Label(window, text="Bare Nuclei",width=20  ,fg=fgcolor  ,bg=bgcolor    ,height=1 ,font=('times', 15, ' bold ')) 
lbl6.place(x=50, y=450)

txt6 = tk.Entry(window,width=15 ,fg=fgcolor,font=('times', 15, ' bold ')  )
txt6.place(x=300, y=450)


lbl7 = tk.Label(window, text="Bland Chromatin",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl7.place(x=50, y=500)

txt7 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt7.place(x=300, y=500)


lbl8 = tk.Label(window, text="Normal Nucleoli",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl8.place(x=600, y=200)

txt8 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt8.place(x=850, y=200)

lbl9 = tk.Label(window, text="Mitoses",width=20  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl9.place(x=600, y=250)

txt9 = tk.Entry(window,width=15,fg=fgcolor,font=('times', 15, ' bold '))
txt9.place(x=850, y=250)

lbl10 = tk.Label(window, text="Predicted Value",width=15  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl10.place(x=600, y=500)

txt10 = tk.Entry(window,width=25,fg=fgcolor,font=('times', 15, ' bold '))
txt10.place(x=850, y=500)


elbl1 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl1.place(x=500, y=200)

elbl2 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl2.place(x=500, y=250)

elbl3 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl3.place(x=500, y=300)

elbl4 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl4.place(x=500, y=350)

elbl5 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl5.place(x=500, y=400)


elbl6 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl6.place(x=500, y=450)


elbl7 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl7.place(x=500, y=500)


elbl8 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl8.place(x=1020, y=200)

elbl9 = tk.Label(window, text="Ex:1-10",width=7  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
elbl9.place(x=1020, y=250)


def preprocess():
	sym="breast-cancer-wisconsin.data"
	if sym != "" :
		pre.process(sym)
		print("preprocess")
		tm.showinfo("Input", "Preprocess Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
	
def train():
	sym="breast-cancer-wisconsin.data"
	if sym != "" :
		tr.process(sym)
		print("preprocess")
		tm.showinfo("Input", "Training Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")
	
def predict():
	print("predict")
	txt10.delete(0, 'end') 
	#txt1.insert('end', "60")
	a1=txt1.get()
	a2=txt2.get()
	a3=txt3.get()
	a4=txt4.get()
	a5=txt5.get()
	a6=txt6.get()
	a7=txt7.get()
	a8=txt8.get()
	a9=txt9.get()
	
	if a1 == "":
		tm.showinfo("Insert error", "Enter Clump Thickness")
	elif a2 == "":
		tm.showinfo("Insert error", "Enter Uniformity of Cell Size")
	elif a3 == "":
		tm.showinfo("Insert error", "Enter Uniformity of Cell Shape")
	elif a4 == "":
		tm.showinfo("Insert error", "Enter Marginal Adhesion")
	elif a5 == "":
		tm.showinfo("Insert error", "Enter Single Epithelial Cell Size")
	elif a6 == "":
		tm.showinfo("Insert error", "Enter Bare Nuclei")
	elif a7 == "":
		tm.showinfo("Insert error", "Enter Bland Chromatin")
	elif a8 == "":
		tm.showinfo("Insert error", "Enter Normal Nucleoli")
	elif a9 == "":
		tm.showinfo("Insert error", "Enter Mitoses")
	else:
		model = load_model('breast-cancer.h5')
		#new_pred = model.predict_classes(np.array([[5,1,1,1,2,1,3,1,1]]))  #2
		new_pred = model.predict_classes(np.array([[a1,a2,a3,a4,a5,a6,a7,a8,a9]]))
		res=new_pred[0]
		print(res)
		if res[0] == 0:
			txt10.insert('end', "Benign")
		else:
			txt10.insert('end', "Malignant")

		
    


 
#process = tk.Button(window, text="Preprocess", command=preprocess  ,fg="white"  ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#process.place(x=50, y=600)

#train = tk.Button(window, text="Train Dataset", command=train  ,fg="white"  ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
#train.place(x=300, y=600)

predict = tk.Button(window, text="Predict", command=predict  ,fg="white"  ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
predict.place(x=200, y=600)

clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=500, y=600)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=800, y=600)

 
window.mainloop()


