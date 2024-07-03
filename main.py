from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")   # layout for Screen
        self.root.title("Face Recognition System")   # title of page

        
        
        # First Top Image
        img=Image.open(r"images\top1.jpg")
        img=img.resize((1530,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        
        #Background Imageg
        img3=Image.open(r"images\bg.jpg")
        img3=img3.resize((1530,660), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=660)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=40)

        # =================Dispaly Time ==================
        def time():
            string =strftime("%d-%b-%Y  %H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl =Label(title_lbl, font =('time new roman', 10,'bold'), background='white',foreground='blue')
        lbl.place(x=1200,y=(-7),width=300, height=50)
        time()

        


        #student button
        img4=Image.open(r"images\students.png")
        img4=img4.resize((150,150), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=50,y=80,width=150,height=150)
        b1=Button(bg_img,text="Emp/Stud Details", command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="#fcba03",fg="red")
        b1.place(x=50,y=230,width=150,height=40)


        #Face Detect button
        img5=Image.open(r"images\fr6.jpg")
        img5=img5.resize((150,150), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=250,y=80,width=150,height=150)
        b1=Button(bg_img,text="Face Detector", command=self.face_data, cursor="hand2",font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=250,y=230,width=150,height=40)


        #Attendance button
        img6=Image.open(r"images\fr2.jpg")
        img6=img6.resize((150,150), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=1150,y=80,width=150,height=150)
        b1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=1150,y=230,width=150,height=40)
        

        #help/Support button
        img7=Image.open(r"images\support.jpg")
        img7=img7.resize((150,150), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1350,y=80,width=150,height=150)
        b1=Button(bg_img,text="Help/Support", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=1350,y=230,width=150,height=40)


        #Training Data Set button
        img8=Image.open(r"images\train.jpg")
        img8=img8.resize((150,150), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=50,y=350,width=150,height=150)
        b1=Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=50,y=500,width=150,height=40)

        # Photos button
        img9=Image.open(r"images\fr10.jpg")
        img9=img9.resize((150,150), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=250,y=350,width=150,height=150)
        b1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=250,y=500,width=150,height=40)
        
        #Developer button
        img10=Image.open(r"images\sandeep.jpg")
        img10=img10.resize((150,150), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=1150,y=350,width=150,height=150)
        b1=Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=1150,y=500,width=150,height=40)
        

        # Exist button
        img11=Image.open(r"images\exist.jpg")
        img11=img11.resize((150,150), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1350,y=350,width=150,height=150)
        b1=Button(bg_img,text="Exist", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="#fcba03",fg="red")
        b1.place(x=1350,y=500,width=150,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure Exit!!!",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    #==============================Function Buttons=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()