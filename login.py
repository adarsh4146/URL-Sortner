import mysql.connector
from tkinter import *
from tkinter import messagebox as tmsg
from PIL import Image, ImageTk

con=mysql.connector.connect(host="localhost",user="root",passwd="Adarsh123@",database="shortner")
mcrs=con.cursor()


##create the database
#mcrs.execute("create database shortner")

##create table
# mcrs.execute("create table users_data1(FULLNAME varchar(300),EMAILID VARCHAR(300),CONTACTNO INT(250) AUTO_INCREMENT PRIMARY KEY,password varchar(300))")

class login:
    def __init__(self,root):

            ##root window and main frame
            self.root=root
            self.root.geometry("500x450")
            self.root.maxsize(500,450)
            self.root.title("LOGIN PAGE")

            self.photo2 = ImageTk.PhotoImage(Image.open("bg12.jfif"))
            Label(self.root, image=self.photo2).place(x=1, y=1, relwidth=1, relheight=1)

            l1=LabelFrame(self.root,bg="white",width=100)
            l1.pack(side=TOP,pady=70,fill=BOTH)

            Url_label=Label(self.root,text="URL SHORTNER",font=("times new roman",25,"bold"),fg="Blue")
            Url_label.place(x=120,y=5)

            l4 = Label(l1, text="Log into URL", font=("times new roman", 20), bg="White", fg="Black")
            l4.grid(row=1, column=2)

            ##Email_label
            l2=Label(l1,text="Email Id",font=("times new roman",17,"bold"),bg="White",fg="gray")
            l2.grid(row=2,column=1)

            ##Entry box for Email
            self.txt_email = Entry(l1, width=20, font=("times new roman",18),bg="silver")
            self.txt_email.grid(row=2, column=2, pady=10)

            ##Password_label
            l3=Label(l1,text="PASSWORD",font=("times new roman",15,"bold"),bg="White",fg="grey")
            l3.grid(row=3,column=1)

            ##Entry box for password
            self.txt_pass=Entry(l1,width=20,font=("times new roman",18),bg="silver",show="*")
            self.txt_pass.grid(row=3,column=2,pady=10)

            ##login Button & create account Button
            Button(l1, text="log in", font=("times new roman", 18, "bold"), command=self.access, bg="cyan", fg="black",cursor="hand2",width=20).grid(row=4, column=2, pady=10)
            Button(l1, text="Create Account", font=("times new roman", 18, "bold"), command=self.create,cursor="hand2").grid(row=5, column=2, pady=10)

    ##window shift to register window
    def create(self):
        self.root.destroy()
        import register

    ##Main_function for access the database and check the user details
    def access(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            tmsg.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", passwd="Adarsh123@", database="shortner")
                mcrs = con.cursor()
                mcrs.execute("select * from users_data1 where EMAILID=%s and PASSWORD=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=mcrs.fetchone()
                if row==None:
                    tmsg.showwarning("Error", "INVALID CREDENTIAL", parent=self.root)
                    exit()
                else:
                    tmsg.showinfo("SUCESS", "WELCOME", parent=self.root)
                con.close()
                self.root.destroy()
                import shorting

            except Exception as es:
                tmsg.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root=Tk()
obj=login(root)
root.mainloop()
