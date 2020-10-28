from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
##databse connection
con=mysql.connector.connect(host="localhost",user="root",passwd="Adarsh123@",database="shortner")
mcrs = con.cursor()
#mcrs.execute("create table users_data1(FULLNAME varchar(300),EMAILID varchar(300),CONTACT_NO int(200),PASSWORD varchar(300),CONFIRM_PASSWORD varchar(300))")


class register:
     def __init__(self,root):
          ##Main_window
          self.root=root
          self.root.title("Registration Window")
          self.root.geometry("1350x700+0+0")
          self.root.config(bg="white")

          ##Insert the background Image
          self.photo1 = ImageTk.PhotoImage(Image.open("bg.jpg"))
          Label(self.root,image=self.photo1).place(x=100,y=0,relwidth=1,relheight=1)

          ##Insert the cover Image
          self.photo2 = ImageTk.PhotoImage(Image.open("tiny.png"))
          Label(self.root, image=self.photo2,bg="cyan").place(x=1, y=100, width=550, height=500)

          ##background colour
          frame1=Frame(self.root,bg="white")
          frame1.place(x=480,y=100,width=600,height=500)

          ##Label for resgister here
          title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="White",fg="green")
          title.place(x=50,y=30)

          ##Full name Label & entry
          f_name=Label(frame1,text="Full Name",font=("times new roman",15,"bold"),bg="White",fg="gray")
          f_name.place(x=50,y=70)
          self.txt_fname=Entry(frame1,font=("times new roman",15),bg="silver")
          self.txt_fname.place(x=50,y=100,width=250)

          ##Email Label & entry
          email = Label(frame1, text="Email Id", font=("times new roman", 15, "bold"), bg="White", fg="gray")
          email.place(x=50, y=130)
          self.e_text = Entry(frame1, font=("times new roman", 15), bg="silver")
          self.e_text.place(x=50, y=160, width=250)

          ##Contact_no Label & entry
          con_no = Label(frame1, text="Contact NO.", font=("times new roman", 15, "bold"), bg="White", fg="gray")
          con_no.place(x=50, y=190)
          self.txt_con = Entry(frame1, font=("times new roman", 15), bg="silver")
          self.txt_con.place(x=50, y=220, width=250)

          ##Password Label & entry
          password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="White", fg="gray")
          password.place(x=50, y=250)
          self.txt_pass = Entry(frame1, font=("times new roman", 15), bg="silver",show="*")
          self.txt_pass.place(x=50, y=280, width=250)

          ##Confirm_password Label & entry
          c_pass = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="White", fg="gray")
          c_pass.place(x=50, y=310)
          self.txt_cpass = Entry(frame1, font=("times new roman", 15), bg="silver",show="*")
          self.txt_cpass.place(x=50, y=340, width=250)

          ##Button for register now
          b_reg=Button(frame1,text="REGISTER NOW", font=("times new roman", 15, "bold"), bg="green", fg="white",cursor="hand2",command=self.register_data)
          b_reg.place(x=50, y=400)

          ##Button for Sign In
          b1=Button(self.root,text="Sign In", font=("times new roman", 20, "bold"),cursor="hand2",command=self.login)
          b1.place(x=200, y=450,width=180)


     ##Function for shift window to login window
     def login(self):
          self.root.destroy()
          import login

     ##Function for clear entry widget after store the data
     def clear(self):
          self.txt_fname.delete(0,END)
          self.e_text.delete(0,END)
          self.txt_con.delete(0,END)
          self.txt_pass.delete(0,END)
          self.txt_cpass.delete(0,END)

     ##Function for check condition if all widget fill so conditon is true
     ##Check if confirm password and password is same then condition is true
     ##Insert the data in database
     def register_data(self):
         if self.txt_fname.get()=="" or self.e_text.get()=="" or self.txt_con.get()=="" or self.txt_pass.get()=="" or self.txt_cpass.get()=="" :
               messagebox.showerror("Error","All Fields Are Required",parent=self.root)
         elif self.txt_pass.get()!=self.txt_cpass.get():
              messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
         else:
              try:
                   con = mysql.connector.connect(host="localhost", user="root", passwd="Adarsh123@",database="shortner")
                   mcrs = con.cursor()
                   mcrs.execute("insert into users_data1 (FULLNAME,EMAILID,CONTACT_NO,PASSWORD) values(%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.e_text.get(),
                                 self.txt_con.get(),
                                 self.txt_pass.get()
                                ))
                   con.commit()
                   con.close()
                   messagebox.showinfo("Sucess", "Register Successful", parent=self.root)
                   self.clear()

              except Exception as es:
                   messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

root=Tk()
obj=register(root)
root.mainloop()

