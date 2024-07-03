from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")   # layout for Screen



        img3=Image.open(r"images\loginbg.jpg")
        img3=img3.resize((1530,790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        login_frame=Frame(self.root,bg="black")
        login_frame.place(x=600,y=170,width=350,height=450)

        img1=Image.open(r"images\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(login_frame,text="Get Started",font=("time new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #UserName
        username=Label(login_frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(login_frame,font=("time new roman",12,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        # Password
        password=Label(login_frame,text="Password",font=("time new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=220)

        self.txtpass=ttk.Entry(login_frame,font=("time new roman",12,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

    # Icon Image =========================
        img2=Image.open(r"images\login.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=640,y=323,width=25,height=25)

        img3=Image.open(r"images\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=640,y=395,width=25,height=25)

        # Login Button
        loginbtn = Button(login_frame, text="Login",command=self.login,font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        # Register Button
        registerbtn = Button(login_frame, text="New User Register",command=self.register_window,font=("time new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=400,width=160)

        # forget Button
        loginbtn = Button(login_frame, text="Forget Password",command=self.forget_password_window,font=("time new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=180,y=400,width=160)
    

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" and self.txtpass.get()=="":
            messagebox,messagebox.showerror("Error","All Field are Required")
        elif self.txtuser.get()=="sandeep" and self.txtpass.get()=="sandy088":
            messagebox,messagebox.showinfo("Success","Welcome to Face Recognition System")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invaild Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authorized Admin")
                if open_main >0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            
            conn.close()
  
    # =========================== Reset Password =========================
    def reset_pass(self):
        if self.securityQ_combo.get()=="Select":
            messagebox.showerror("Error", "Select Security Question !",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer !",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Passwor !",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.securityQ_combo.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row =my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get(),)
                my_cursor.execute(query,value)


                conn.commit()
                conn.close()
                messagebox.showinfo("INfo","Your Password has been reset, Please Login wirh new Password",parent=self.root2)
                self.root2.destroy()


    # ===========================Forget Password window ===================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the vails user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("360x455+610+200")

                l=Label(self.root2,text="Forget Password",font=("time new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10, relwidth=1)

                # Security Question
                securityQ=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="blue")
                securityQ.place(x=50,y=80)

                self.securityQ_combo=ttk.Combobox(self.root2, font=("times new roman",15,"bold"), state="readonly")
                self.securityQ_combo["values"]=("Select","Your Birth place?","What is your Nickname?","Your Pet Name?")
                self.securityQ_combo.place(x=50,y=110,width=250)
                self.securityQ_combo.current(0)
                

                securityA=Label(self.root2,text="Security Answer",font=("time new roman",15,"bold"),fg="blue")
                securityA.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("time new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                newpass=Label(self.root2,text="New Password",font=("time new roman",15,"bold"),fg="blue")
                newpass.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("time new roman",15,"bold"),show="*")
                self.txt_newpass.place(x=50,y=250,width=250)

                resetbtn = Button(self.root2, text="Reset",command=self.reset_pass,font=("time new roman",15,"bold"),fg="white",bg="green",activeforeground="white",activebackground="green")
                resetbtn.place(x=100,y=330,width=120,height=35)



             



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
        img4=Image.open(r"images\reg.jpg")
        img4=img4.resize((670,550), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=50,y=100,width=670,height=550)

        #======main Frame ============
        frame=Frame(self.root,bg="grey")
        frame.place(x=720,y=100,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=0,y=20,width=670)

        # ==================Label and Entry for registation ==============

        fname=Label(frame,text="First Name",font=("time new roman",12,"bold"),fg="black",bg="grey")
        fname.place(x=50,y=90)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",12,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("time new roman",12,"bold"),fg="black",bg="grey")
        lname.place(x=370,y=90)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",12,"bold"))
        self.lname_entry.place(x=375,y=130,width=250)


        contact=Label(frame,text="Contact No.",font=("time new roman",12,"bold"),fg="black",bg="grey")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",12,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("time new roman",12,"bold"),fg="black",bg="grey")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",12,"bold"))
        self.email_entry.place(x=375,y=200,width=250)

         # Security Question
        security_Q=Label(frame,text="Security Question",font=("time new roman",12,"bold"),fg="black",bg="grey")
        security_Q.place(x=50,y=250)

        self.security_Q_combo=ttk.Combobox(frame, textvariable=self.var_securityQ,font=("times new roman",12,"bold"), state="readonly")
        self.security_Q_combo["values"]=("Select","Your Birth place?","What is your Nickname?","Your Pet Name?")
        self.security_Q_combo.place(x=50,y=280,width=300)
        self.security_Q_combo.current(0)
        

        security_A=Label(frame,text="Security Answer",font=("time new roman",12,"bold"),fg="black",bg="grey")
        security_A.place(x=370,y=250)

        self.security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",12,"bold"))
        self.security_A_entry.place(x=370,y=280,width=250)


        pswd=Label(frame,text="Password",font=("time new roman",12,"bold"),fg="black",bg="grey")
        pswd.place(x=50,y=320)

        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",12,"bold"),show="*")
        self.pswd_entry.place(x=50,y=350,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("time new roman",12,"bold"),fg="black",bg="grey")
        confirm_pswd.place(x=370,y=320)

        self.confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",12,"bold"))
        self.confirm_pswd_entry.place(x=375,y=350,width=250)

    #======================CheckBox =====================================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("time new roman",12,"bold"),fg="black",bg="grey",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=390)

    # ====================================buttons =======================
        registerbtn = Button(frame, text="Register",command=self.register_data,font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        registerbtn.place(x=100,y=450,width=120,height=35)


        loginbtn = Button(frame, text="Login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=450,y=450,width=120,height=35)

    # ======================Function Declaration =================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email Already Exist,Please try another email",parent=self.root)
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
    main()
  