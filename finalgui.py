#Final 0.2
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image, ImageDraw
import PIL
import cv2
from sklearn .externals import joblib
import matplotlib.image as  mimage
import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
from sklearn import metrics
from collections import Counter
import finalhindi
import finalenglishdigit
from finalenglishdigit import *
from finalhindi import *
import finalhindidigit
import finalenglish
from finalenglish import *
from finalhindidigit import *
from tkinter import filedialog

""" FIRST WINDOW"""
class Buttons:
    def __init__(self, master):
        
        self.master = master
        self.frame = Frame(self.master, width=500, height=300)
        self.L1 = Label(self.master, text="WELCOME")
        self.L1.pack()
        self.b1 = Button(self.master, text="Hindi Characters", command=self.HChar)
        self.b2 = Button(self.master, text="English Characters", command=self.EChar)
        self.b3 = Button(self.master, text="Hindi Digits", command=self.HDigi)
        self.b4 = Button(self.master, text="English Digits", command=self.EDigi)
        self.b5 = Button(self.master,text='Exit',command=self.master.destroy,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        self.frame.pack()
        self.b1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.b2.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.b3.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.b4.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.b5.place(relx=0.8, rely=0.8, anchor=CENTER)
        
    def HChar(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)   # object formation
        HindiChar(self.newWindow)    #class calling
    def EChar(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)   # object formation
        EnglishChar(self.newWindow)    #class calling
    def HDigi(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)   # object formation
        HindiDigit(self.newWindow)    #class calling
    def EDigi(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)   # object formation
        EnglishDigit(self.newWindow)    #class calling

""" HINDI CHARACTERS WINDOW  """
class HindiChar():
    def __init__(self, master):
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.master = master
        self.frame = Frame(self.master,width=800, height=600)
        self.frame.pack()

        self.Back= Button(self.frame, text = "BACK", command = self.back)     # Back button 
        self.Back.grid(row=6, column=3)
    
        self.c = Canvas(self.frame, bg='WHITE', width=200, height=200, borderwidth=3,relief='raised')   
        self.c.grid(row=1, columnspan=3)# first canvas
        
        self.c.bind("<Motion>", self.motion)
        self.c.bind("<ButtonPress-1>", self.b1down)
        self.c.bind("<ButtonRelease-1>", self.b1up)
        
        self.b3 = Button(self.frame,text='Exit',command=self.master.destroy,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        self.b3.grid(row=3, column=3)     # Exit Butoon

        self.clear = Button(self.frame, text = "Clear Screen", command= self.dele)  #clear screen button
        self.clear.grid(row=2, column = 1)

        self.upload=Button(self.frame, text="Upload File",command = self.upload)    #upload file button
        self.upload.grid(row=1, column = 3)

        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

        self.pred = Button(self.frame, text="Predict",command = self.pred)    #Predict  Button 
        self.pred.grid(row=2, column = 3)

    def upload(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PNG files","*.png"),("all files","*.*")))
        self.gif1 = PhotoImage(file = self.filename)
        x=self.filename
        #self.c.create_image(0,0,image = self.gif1, anchor = NW)
        finalhindi.final_predict()
    def pred(self):                                      #Predict function
        filename = "image1.png"
        self.image.save(filename)
        finalhindi.final_predict()
        
    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='false',width=7,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,0,0),width=10)

        self.xold = event.x
        self.yold = event.y

    def back(self):                     #Back function
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Buttons(self.newWindow)

    def dele(self):                                                  #clear screen function
        self.c.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
    

""" ENGLISH CHARACTERS WINDOW"""
class EnglishChar():
    def __init__(self, master):
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.master = master
        self.frame = Frame(self.master,width=800, height=600)
        self.frame.pack()

        self.Back= Button(self.frame, text = "BACK", command = self.back)     # Back button 
        self.Back.grid(row=6, column=3)
    
        self.c = Canvas(self.frame, bg='WHITE', width=200, height=200, borderwidth=3,relief='raised')   
        self.c.grid(row=1, columnspan=3)# first canvas
        self.c.bind("<Motion>", self.motion)
        self.c.bind("<ButtonPress-1>", self.b1down)
        self.c.bind("<ButtonRelease-1>", self.b1up)
        
        self.b3 = Button(self.frame,text='Exit',command=self.master.destroy,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        self.b3.grid(row=5, column=3)     # Exit Butoon

        self.clear = Button(self.frame, text = "Clear Screen", command= self.dele)  #clear screen button
        self.clear.grid(row=2, column = 1)

        self.upload=Button(self.frame, text="Upload File")    #upload file button
        self.upload.grid(row=1, column = 3)
        
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

        self.saveb = Button(self.frame, text="Predict",command = self.pred)    #Predict  Button 
        self.saveb.grid(row=2, column = 3)

    def pred(self):                                      #Predict function
        filename = "image1.png"
        self.image.save(filename)
        finalenglish.final_predict()
        
    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='false',width=7,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,0,0),width=15)

        self.xold = event.x
        self.yold = event.y

    def back(self):                     #Back function
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Buttons(self.newWindow)

    def dele(self):                                                  #clear screen function
        self.c.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
    

""" HINDI DIGITS WINDOW  """
class HindiDigit():
    def __init__(self, master):
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.master = master
        self.frame = Frame(self.master,width=800, height=600)
        self.frame.pack()

        self.Back= Button(self.frame, text = "BACK", command = self.back)     # Back button 
        self.Back.grid(row=6, column=3)
    
        self.c = Canvas(self.frame, bg='WHITE', width=200, height=200, borderwidth=3,relief='raised')   
        self.c.grid(row=1, columnspan=3)# first canvas
        self.c.bind("<Motion>", self.motion)
        self.c.bind("<ButtonPress-1>", self.b1down)
        self.c.bind("<ButtonRelease-1>", self.b1up)
        
        self.b3 = Button(self.frame,text='Exit',command=self.master.destroy,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        self.b3.grid(row=5, column=3)     # Exit Butoon

        self.clear = Button(self.frame, text = "Clear Screen", command= self.dele)  #clear screen button
        self.clear.grid(row=2, column = 1)

        self.upload=Button(self.frame, text="Upload File")    #upload file button
        self.upload.grid(row=1, column = 3)

        
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

        self.saveb = Button(self.frame, text="Predict",command = self.pred)    #Predict  Button 
        self.saveb.grid(row=2, column = 3)

    def pred(self):                                      #Predict function
        filename = "image1.png"
        self.image.save(filename)
        finalhindidigit.final_predict()
        
    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='false',width=7,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,0,0),width=15)

        self.xold = event.x
        self.yold = event.y

    def back(self):                     #Back function
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Buttons(self.newWindow)

    def dele(self):                                                  #clear screen function
        self.c.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
        

""" ENGLISH DIGITS WINDOW  """
class EnglishDigit():
    def __init__(self, master):
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.master = master
        self.frame = Frame(self.master,width=800, height=600)
        self.frame.pack()

        self.Back= Button(self.frame, text = "BACK", command = self.back)     # Back button 
        self.Back.grid(row=6, column=3)
    
        self.c = Canvas(self.frame, bg='WHITE', width=200, height=200, borderwidth=3,relief='raised')   
        self.c.grid(row=1, columnspan=3)# first canvas
        
        self.c.bind("<Motion>", self.motion)
        self.c.bind("<ButtonPress-1>", self.b1down)
        self.c.bind("<ButtonRelease-1>", self.b1up)
        
        self.b3 = Button(self.frame,text='Exit',command=self.master.destroy,activebackground='grey',activeforeground='#AB78F1',bg='#58F0AB',highlightcolor='red',padx='10px',pady='3px')
        self.b3.grid(row=5, column=3)     # Exit Butoon

        self.clear = Button(self.frame, text = "Clear Screen", command= self.dele)  #clear screen button
        self.clear.grid(row=2, column = 1)

        self.upload=Button(self.frame, text="Upload File")    #upload file button
        self.upload.grid(row=1, column = 3)

        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

        self.saveb = Button(self.frame, text="Predict",command = self.pred)    #Predict  Button 
        self.saveb.grid(row=2, column = 3)

    def pred(self):                                      #Predict function
        filename = "image1.png"
        self.image.save(filename)
        finalenglishdigit.final_englishdigit()
        
    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true',width=7,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,0,0),width=20)

        self.xold = event.x
        self.yold = event.y

    def back(self):                     #Back function
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Buttons(self.newWindow)

    def dele(self):                                                  #clear screen function
        self.c.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
        

"""MAIN CALLING"""        
if __name__ == '__main__':
    root = Tk()
    b = Buttons(root)
    root.mainloop()
