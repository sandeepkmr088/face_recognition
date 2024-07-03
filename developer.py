from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER - SANDEEP KUMAR",font=("times new roman",24,"bold"),bg="green",fg="white")
        title_lbl.place(x=0,y=0,width=1530, height=40)

        backbtn = Button(title_lbl, text="Closed This Window",command=self.iExit,font=("time new roman",10,"bold"),fg="white",bg="red",activeforeground="white",activebackground="red")
        backbtn.place(x=1300,y=5,width=220)


        img_top=Image.open(r"images\developer.jpeg")
        img_top=img_top.resize((1530,720), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1530,height=720)

        # Frame for Developer Informartion

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"images\sandeep.jpg")
        img_top1=img_top1.resize((200,250), Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=5,width=200,height=250)

        # Developer Ingo
        dep_label=Label(main_frame,text="Sandeep Kumar",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="Software Engineer",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=40)

        dep_label=Label(main_frame,text="Freelancer",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=80)

        dep_label=Label(main_frame,text="I am full stack developer",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=120)

        dep_label=Label(main_frame,text="Java, Spring, Python, Django",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=160)

        dep_label=Label(main_frame,text="Data Analysis and Data Visualization",font=("times new roman",12,"bold"),fg="blue", bg="white")
        dep_label.place(x=0,y=200)

        img2=Image.open(r"images\support1.jpg")
        img2=img2.resize((500,390), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=240,width=500,height=390)
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure Exit from this Window!!!",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()  