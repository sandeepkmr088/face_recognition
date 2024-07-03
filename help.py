from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"images\top1.jpg")
        img=img.resize((1530,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        title_lbl=Label(self.root,text="HELP & SUPPORT",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530, height=40)

    

        img_top=Image.open(r"images\help.jpg")
        img_top=img_top.resize((1530,610), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=170,width=1530,height=610)

         # Developer Ingo
        dep_label=Label(f_lbl,text="Email: sandeep.kumar@cdac.in",font=("times new roman",24,"bold"),fg="blue", bg="white")
        dep_label.place(x=600,y=150)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()  