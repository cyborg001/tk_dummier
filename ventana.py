#-*- encoding: utf-8 -*-
import sys
from Tkinter import *


root = Tk()
def callback():
	print("hola mundo!")
b = Button(root, text='ok', command=callback)
b.pack()





root.mainloop()
