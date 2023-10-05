from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


root= Tk()

root= Tk()
root.title('BMI calculator')
root.geometry('470x580+300+200')
root.resizable(False, False)
root.configure(bg="#f0f1f5")

#icon image
image_icon=PhotoImage(file="img/bmi.png")
root.iconphoto(False,image_icon)

#top image
top=PhotoImage(file="img/top.png")
top_image=Label(root,image=top,background='#f0f1f5')
top_image.place(x=20,y=5)




root.mainloop()