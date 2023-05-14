# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:54:31 2023

@author: ROCKJUNIOR ROMAN
"""

#importing whole module
from tkinter import *
from tkinter.ttk import *
#importing strftime fuction to
#retrieve system's window
from time import strftime
#creating tkinter window
root = Tk()
root.title('clock')
#This function is used to
#display time on label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
#styling the label widget so that clock
#will look more attractive
lbl = label(root, font = ('calbri', 40, 'bold'),
            background = 'black',
            foreground = 'white')
#Placing clock at the centre
#of the tkinter window
lbl.pack(anchor = 'center')
time()
mainloop()
