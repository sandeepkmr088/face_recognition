from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import tkinter





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


       
        img_top=Image.open(r"images\top1.jpg")
        img_top=img_top.resize((1530,130), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530, height=40)

        backbtn = Button(title_lbl, text="Closed This Window",command=self.iExit,font=("time new roman",10,"bold"),fg="white",bg="red",activeforeground="white",activebackground="red")
        backbtn.place(x=1300,y=5,width=220)
        
        img_bottom=Image.open(r"images\bg.jpg")
        img_bottom=img_bottom.resize((1530,610), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=170,width=1530,height=610)

        b1=Button(f_lbl,text="TRAIN DATA",command=self.tain_classifier,cursor="hand2",font=("times new roman",20,"bold"),fg="black",bg='#c97c00',activeforeground="black",activebackground="#c97c00")
        b1.place(x=600,y=270,width=350,height=45)

    
    def tain_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # gray scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #============== Train the Classifier and Save ==========
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Sets Completed!!",parent=self.root)
        

    
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure Exit from this Window!!!",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return  





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        