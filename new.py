from tkinter import *
import pyshorteners
from PIL import Image,ImageTk
from tkinter import  messagebox as tmsg

class short:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome To My URL SHORTNER")
        self.root.geometry("1400x1000+0+0")
        self.root.config(bg="white")
        main_frame=Frame(self.root)
        main_frame.pack(fill=BOTH,expand=1)
        self.photo2 = ImageTk.PhotoImage(Image.open("tiny3.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("tiny2.png"))

        my_canvas=Canvas(main_frame)
        my_canvas.pack(fill=BOTH,expand=1)
        Label(my_canvas, image=self.photo2,bg="white").place(x=1,y=1,)
        Label(my_canvas, image=self.photo3,bg="white").place(x=1,y=1)

        frame2=Frame(my_canvas,bg="Teal")
        frame2.place(x=1, y=450, width=1550, height=200)
        frame3 = Frame(my_canvas, bg="blue")
        frame3.place(x=1, y=730, width=1550, height=100)
        label=Label(my_canvas,text="enter url" ,font=("times new roman", 20, "bold"), bg="White", fg="black")
        label.place(x=180, y=460)
        label1 = Label(my_canvas, text="Copyright © 2002-2020 TinyURL, LLC. All rights reserved.\nTinyURL is a trademark of TinyURL, LLC.", font=("times new roman", 20, "bold"), bg="blue")
        label1.place(x=10, y=730)
        label2 = Label(my_canvas,text="Privacy policy",font=("times new roman", 20, "underline","bold"), bg="blue",cursor="hand2")
        label2.place(x=1150, y=730)


        self.txt_short = Entry(my_canvas,  width=70, font=("times new roman", 20), bg="white")
        self.txt_short.place(x=300, y=460)
        button=Button(my_canvas, text="shorturl",font=("times new roman", 20, "bold"),bg="navy blue",fg="white",cursor="hand2",command=self.url)
        button.place(x=670, y=520,width=200)
        button1 = Button(my_canvas, text="Copy", font=("times new roman", 20, "bold"), bg="navy blue", fg="white",cursor="hand2", command=self.copy_text)
        button1.place(x=900, y=590, width=200)

    def copy_text(self):
        global selected
        if my_text.selected_get():
            selected=self.label.selected_get()

    def url(self):
        if self.txt_short.get()=="":
            tmsg.showerror("url","Url Required")
        else:
            row=self.txt_short.get()
            shortner = pyshorteners.Shortener()
            x = shortner.tinyurl.short(row)
            label=Entry(self.root,font=("times new roman", 20, "bold"), bg="White", fg="black")
            label.place(x=550,y=590,width=500)
            label.insert(0,x)
            label.config(state="readonly")

root=Tk()
obj=short(root)
root.mainloop()