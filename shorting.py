from tkinter import *
import pyshorteners
from PIL import Image,ImageTk
from tkinter import  messagebox as tmsg

class short:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome To My URL SHORTNER")
        self.root.geometry("1800x1000")
        self.root.config(bg="white")
        main_frame=Frame(self.root)
        main_frame.pack(fill=BOTH,expand=1)
        self.photo2 = ImageTk.PhotoImage(Image.open("tiny3.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("tiny2.png"))
        self.photo4 = ImageTk.PhotoImage(Image.open("download.png"))
        self.photo5 = ImageTk.PhotoImage(Image.open("brand2.png"))
        self.photo6 = ImageTk.PhotoImage(Image.open("br1.jpg"))
        self.photo7 = ImageTk.PhotoImage(Image.open("Nike.jpg"))

        my_canvas=Canvas(main_frame)
        my_canvas.pack(fill=BOTH,expand=1)
        Label(my_canvas, image=self.photo2,bg="white").place(x=1,y=1,)
        Label(my_canvas, image=self.photo3,bg="white").place(x=1,y=1)
        Label(my_canvas, image=self.photo4,bg="white").place(x=1,y=500,width=200,height=300)
        Label(my_canvas, image=self.photo5,bg="white").place(x=280,y=530)
        Label(my_canvas, image=self.photo6,bg="white").place(x=550,y=530,width=530,height=300)
        Label(my_canvas, image=self.photo7,bg="white").place(x=1060,y=500,width=530,height=300)

        frame2=Frame(my_canvas,bg="Teal")
        frame2.place(x=1, y=325, width=1550, height=200)
        frame3 = Frame(my_canvas, bg="blue")
        frame3.place(x=1, y=770, width=1550, height=100)
        label=Label(my_canvas,text="enter url" ,font=("times new roman", 20, "bold"), bg="White", fg="black")
        label.place(x=180, y=340)
        label1 = Label(my_canvas, text="Copyright © 2002-2020 TinyURL, LLC. All rights reserved.\nTinyURL is a trademark of TinyURL, LLC.", font=("times new roman", 20, "bold"), bg="blue")
        label1.place(x=10, y=770)
        label2 = Label(my_canvas,text="Privacy policy",font=("times new roman", 20, "underline","bold"), bg="blue",cursor="hand2")
        label2.place(x=1150, y=770)
        label1 = Label(my_canvas,text="The most recognized brands in the world love Tiny.",font=("times new roman", 20, "bold"), fg="black",bg="white")
        label1.place(x=455, y=525)

        self.txt_short = Entry(my_canvas,  width=70, font=("times new roman", 20), bg="white")
        self.txt_short.place(x=300, y=340)
        button=Button(my_canvas, text="shorturl",font=("times new roman", 20, "bold"),bg="navy blue",fg="white",cursor="hand2",command=self.url)
        button.place(x=670, y=390,width=200)


    def url(self):
        if self.txt_short.get()=="":
            tmsg.showerror("url","Url Required")
        else:
            row=self.txt_short.get()
            shortner = pyshorteners.Shortener()
            x = shortner.tinyurl.short(row)
            label = Entry(self.root, font=("times new roman", 20, "bold"), bg="White", fg="black")
            label.place(x=600, y=460, width=400)
            label.insert(0, x)
            label.config(state="readonly")


root=Tk()
obj=short(root)
root.mainloop()

