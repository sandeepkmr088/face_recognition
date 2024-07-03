from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
import datetime
from datetime import datetime
import cv2
import os
import os.path
import pandas as pd
from pathlib import Path
import csv
from csv import reader





class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"images\top1.jpg")
        img=img.resize((1530,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530, height=40)

        
        
        # ================date and Time =============================
        def time():
            string =strftime("%d-%b-%Y  %H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl =Label(title_lbl, font =('time new roman', 10,'bold'), background='white',foreground='blue')
        lbl.place(x=1200,y=(-7),width=300, height=50)
        time()
        
        # First Image
        img_top=Image.open(r"images\face02.jpg")
        img_top=img_top.resize((765,620), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=170,width=765,height=620)
        
        # Second Image
        img_next=Image.open(r"images\faceR01.jpg")
        img_next=img_next.resize((765,620), Image.ANTIALIAS)
        self.photoimg_next=ImageTk.PhotoImage(img_next)

        f_lb1=Label(self.root,image=self.photoimg_next)
        f_lb1.place(x=765,y=170,width=765,height=620)

      
        # Button
        b1=Button(f_lb1,text="Face Recognition-IN",command=self.face_recog_in,cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white")
        b1.place(x=250,y=90,width=255,height=30)

        b1=Button(f_lb1,text="Face Recognition-OUT",command=self.face_recog_out,cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white")
        b1.place(x=250,y=525,width=255,height=30)

    #==========Attendance IN TIME =================
    def csv_file_IN_TIME(self):
        now=datetime.now()
        file='AIT'+now.strftime("%Y%m%d")+'.csv'
        df = pd.DataFrame(list())   # columns=['City', 'State']
        df.to_csv(file,header=0) # create new csv file
               
    def mark_attendance_in(self,i, n, r):
        now=datetime.now()
        PATH='AIT'+now.strftime("%Y%m%d")+'.csv'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print( "File exists and is readable/there")
    
            with open(PATH,"r+") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((i not in name_list)) and ((n not in name_list)) and ((r not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%Y-%m-%d")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{n},{r},{dtString},{d1},IN-Time")
        else:
            self.csv_file_IN_TIME()           
              


    # =======Face Recognition IN TIME ==============

    def face_recog_in(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select studentId from student where studentId="+str(id))
                i=my_cursor.fetchone()
                i="+".join(map(str,i))

                my_cursor.execute("select name from student where studentId="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where studentId="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                if confidence>83:
                    cv2.putText(img,f"Id: {i}",(x,y+280),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    cv2.putText(img,f"Name: {n}",(x,y+310),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    cv2.putText(img,f"Roll No: {r}",(x,y+340),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    self.mark_attendance_in(i,n,r)
                  #  try:
                    now=datetime.now()
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    cursor=conn.cursor()
                    with open('AIT'+now.strftime("%Y%m%d")+'.csv','r+') as csv_file:
                        csv_reader = reader(csv_file)
                        header = next(csv_reader)
                        csvfile = csv.reader(csv_file,delimiter=',')
                        for row in csvfile:
                            #  q="insert into ait (studentId,name,roll,time,date,status) values ('Null','Null','Null','Null',CURDATE(),'Null')"
                            #  cursor.execute(q,row)
                            query ="insert ignore into ait (studentId,name,roll,time,date,status) values (%s,%s,%s,%s,%s,%s)"
                            #query="update ait set studentID=%s, name=%s, roll=%s,time=%s,date=%s,status=%s where date=curdate()"
                            cursor.execute(query,row)
                            print(row)
                    conn.commit()
                    conn.close()
                 #   except Exception as es:
                 #      messagebox.showerror("Error",f"Problem in database side:{str(es)}", parent=self.root)
                   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknow Face",(x,y+255),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)

                coord=[x,y,w,h]
           
                  
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.3,10,(255,25,255),"Face", clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")   
        

        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        while(video_cap.isOpened()):
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

     #==========Attendance OUT TIME =================
        
    def csv_file_OUT_TIME(self):
        now=datetime.now()
        df = pd.DataFrame(list())
        df.to_csv('AOT'+now.strftime("%Y%m%d")+'.csv',header=0) # create new csv file
               
    def mark_attendance_out(self,i, n, r):
        now=datetime.now()
        PATH='AOT'+now.strftime("%Y%m%d")+'.csv'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print( "File exists and is readable/there")

          
            with open(PATH,"r+",encoding='UTF8',newline='') as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((i not in name_list)) and ((n not in name_list)) and ((r not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%Y-%m-%d")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{n},{r},{dtString},{d1},OUT-Time")

        else:
            self.csv_file_OUT_TIME()           
              
      

    # =======Face Recognition OUT TIME ==============

    def face_recog_out(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select studentId from student where studentId="+str(id))
                i=my_cursor.fetchone()
                i="+".join(map(str,i))

                my_cursor.execute("select name from student where studentId="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where studentId="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                

                if confidence>83:
                    cv2.putText(img,f"Id: {i}",(x,y+280),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    cv2.putText(img,f"Name: {n}",(x,y+310),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    cv2.putText(img,f"Roll No: {r}",(x,y+340),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),3)
                    self.mark_attendance_out(i,n,r)
                    #try:
                    now=datetime.now()
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    cursor=conn.cursor()
                    with open('AOT'+now.strftime("%Y%m%d")+'.csv','r+') as csv_file:
                        csv_reader = reader(csv_file)
                        header = next(csv_reader)
                        csvfile = csv.reader(csv_file,delimiter=',')
                        for row in csvfile:
                            query ="insert ignore into aot (studentId,name,roll,times,date,status) values (%s,%s,%s,%s,%s,%s)"
                            cursor.execute(query,row)
                            print(row)
                    conn.commit()
                    conn.close()
                   # except Exception as es:
                   #     messagebox.showerror("Error",f"Due To Database:{str(es)}", parent=self.root)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknow Face",(x,y+255),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)

                coord=[x,y,w,h]
               
                
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.2,10,(255,25,255),"Face", clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        while(video_cap.isOpened()):
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()    