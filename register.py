from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")   # layout for Screen

        # ============= variable ==========

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        

        # ==============Background Iamge ==============
        img3=Image.open(r"images\loginbg.jpg")
        img3=img3.resize((1530,790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        # ==============left Iamge ==============
        img4=Image.open(r"images\loginbg.jpg")
        img4=img4.resize((670,550), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=50,y=100,width=670,height=550)

        #======main Frame ============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ==================Label and Entry for registation ==============

        fname=Label(frame,text="First Name",font=("time new roman",15,"bold"),fg="blue")
        fname.place(x=50,y=90)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("time new roman",15,"bold"),fg="blue")
        lname.place(x=370,y=90)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",15,"bold"))
        self.lname_entry.place(x=375,y=130,width=250)


        contact=Label(frame,text="Contact No.",font=("time new roman",15,"bold"),fg="blue")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("time new roman",15,"bold"),fg="blue")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",15,"bold"))
        self.email_entry.place(x=375,y=200,width=250)

         # Security Question
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="blue")
        security_Q.place(x=50,y=250)

        self.security_Q_combo=ttk.Combobox(frame, textvariable=self.var_securityQ,font=("times new roman",15,"bold"), state="readonly")
        self.security_Q_combo["values"]=("Select","Your Birth place?","What is your Nickname?","Your Pet Name?")
        self.security_Q_combo.place(x=50,y=280,width=300)
        self.security_Q_combo.current(0)
        

        security_A=Label(frame,text="Security Answer",font=("time new roman",15,"bold"),fg="blue")
        security_A.place(x=370,y=250)

        self.security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",15,"bold"))
        self.security_A_entry.place(x=370,y=280,width=250)


        pswd=Label(frame,text="Password",font=("time new roman",15,"bold"),fg="blue")
        pswd.place(x=50,y=320)

        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",15,"bold"))
        self.pswd_entry.place(x=50,y=350,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("time new roman",15,"bold"),fg="blue")
        confirm_pswd.place(x=370,y=320)

        self.confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",15,"bold"))
        self.confirm_pswd_entry.place(x=375,y=350,width=250)

    #======================CheckBox =====================================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("time new roman",10,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=390)

    # ====================================buttons =======================
        registerbtn = Button(frame, text="Register",command=self.register_data,font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        registerbtn.place(x=100,y=450,width=120,height=35)


        loginbtn = Button(frame, text="Login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=450,y=450,width=120,height=35)

    # ======================Function Declaration =================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email Already Exist,Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                      ))
    

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Register Successfully",parent=self.root)       










if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()