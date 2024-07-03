from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import pandas as pd
from time import strftime
import datetime
from datetime import datetime


mydata=[]
mydata_FAS=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=======================Variables ==============
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_status=StringVar()
       
        

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

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",24,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=40,width=1530,height=660)

        #left side Frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10, width=765,height=600)

        img_left=Image.open(r"images\attendance1.png")
        img_left=img_left.resize((764,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=765,height=130)


        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=760,height=400)

        # Label and Entry

        # Attendance ID
        attendanceId_label=Label(left_inside_frame,text="AttendanceID",font=("times new roman",12,"bold"))
        attendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceID_entry=Entry(left_inside_frame,width=15,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # Name
        nameLabel_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"))
        nameLabel_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        nameLabel_entry=Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        nameLabel_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Roll No
        rollLabel_label=Label(left_inside_frame,text="Roll No",font=("times new roman",12,"bold"))
        rollLabel_label.grid(row=0,column=4,padx=5,pady=5,sticky=W)

        rollLabel_entry=Entry(left_inside_frame,width=15,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        rollLabel_entry.grid(row=0,column=5,padx=5,pady=5,sticky=W)

       

         # time
        timeLabel_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"))
        timeLabel_label.grid(row=1,column=0,padx=5,pady=20,sticky=W)

        timeLabel_entry=Entry(left_inside_frame,width=15,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        timeLabel_entry.grid(row=1,column=1,padx=5,pady=20,sticky=W)

         # date
        dateLabel_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"))
        dateLabel_label.grid(row=1,column=2,padx=5,pady=20,sticky=W)

        dateLabel_entry=Entry(left_inside_frame,width=15,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        dateLabel_entry.grid(row=1,column=3,padx=5,pady=20,sticky=W)

         # Attendance
        attendanceLabel_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"))
        attendanceLabel_label.grid(row=1,column=4,padx=5,pady=20,sticky=W)


        self.atten_status=ttk.Combobox(left_inside_frame, width=15,textvariable=self.var_attend_status,font=("times new roman",12,"bold"), state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=1,column=5,pady=20)
        self.atten_status.current(0)
        
         #button Frame
        first_btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        first_btn_frame.place(x=0,y=250,width=764,height=500)
        
        reset_btn=Button(first_btn_frame,text="Merge All CSV Files",command=self.mergeCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=0,pady=5)

        reset_btn=Button(first_btn_frame,text="Export CSV Data to Database",command=self.csv_data_export_database,width=22,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=1,pady=5)

        reset_btn=Button(first_btn_frame,text="Import Final Attendance Sheet from Database",command=self.data_import_database,width=36,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2,pady=5)
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=310,width=764,height=250)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=1,column=0,pady=5)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=1,column=1,pady=5)

        delete_btn=Button(btn_frame,text="Delete",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=1 ,column=3,pady=5)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=4,pady=5)

        reset_btn=Button(btn_frame,text="Show Final Attendance",command=self.importCsv_FAS,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=5,pady=5)

        

        #Right side Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Information", font=("times new roman",12,"bold"))
        Right_frame.place(x=764,y=10, width=750,height=240)

        #img_right=Image.open(r"D:\face_recognition_system\images\emp6.jpg")
        #img_right=img_right.resize((763,130), Image.ANTIALIAS)
        #self.photoimg_right=ImageTk.PhotoImage(img_right)

        #f_lbl=Label(Right_frame,image=self.photoimg_right)
        #f_lbl.place(x=5,y=0,width=764,height=130)

        table_frame=Frame(Right_frame,bd=2,bg="yellow",relief=RIDGE)
        table_frame.place(x=5,y=10, width=740,height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReport_table=ttk.Treeview(table_frame,column=("id","name","roll","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)

        self.AttendanceReport_table.heading("id",text="Attendance ID")
        self.AttendanceReport_table.heading("name",text="name")
        self.AttendanceReport_table.heading("roll",text="Roll No")
        self.AttendanceReport_table.heading("time",text="Time")
        self.AttendanceReport_table.heading("date",text="Date")
        self.AttendanceReport_table.heading("attendance",text="Attendance Status")

        self.AttendanceReport_table["show"]="headings"
        self.AttendanceReport_table.column("id",width=100)
        self.AttendanceReport_table.column("name",width=100)
        self.AttendanceReport_table.column("roll",width=100)
        self.AttendanceReport_table.column("time",width=100)
        self.AttendanceReport_table.column("date",width=100)
        self.AttendanceReport_table.column("attendance",width=100)

        self.AttendanceReport_table.pack(fill=BOTH,expand=1)

        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)




        Right_frame1=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Final Attendance Sheet", font=("times new roman",12,"bold"))
        Right_frame1.place(x=764,y=260, width=750,height=370)

        table_frame1=Frame(Right_frame1,bd=2,bg="yellow",relief=RIDGE)
        table_frame1.place(x=5,y=10, width=740,height=320)

        scroll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)

        self.FinalAttendance_table=ttk.Treeview(table_frame1,column=("sno","studentId","name","roll","in_time","out_time","date","total_time","status","leave_applied"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.FinalAttendance_table.xview)
        scroll_y.config(command=self.FinalAttendance_table.yview)

        self.FinalAttendance_table["show"]="headings"
        self.FinalAttendance_table.column("sno",width=100)
        self.FinalAttendance_table.column("studentId",width=100)
        self.FinalAttendance_table.column("name",width=100)
        self.FinalAttendance_table.column("roll",width=100)
        self.FinalAttendance_table.column("in_time",width=100)
        self.FinalAttendance_table.column("out_time",width=100)
        self.FinalAttendance_table.column("date",width=100)
        self.FinalAttendance_table.column("total_time",width=100)
        self.FinalAttendance_table.column("status",width=100)
        self.FinalAttendance_table.column("leave_applied",width=100)


        self.FinalAttendance_table.pack(fill=BOTH,expand=1)

        self.FinalAttendance_table.bind("<ButtonRelease>",self.get_cursor)


    # ============================Fetch Data ============================

    def fetchData(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)
    
    def fetchData_FAS(self,rows):
        self.FinalAttendance_table.delete(*self.FinalAttendance_table.get_children())
        for i in rows:
            self.FinalAttendance_table.insert("",END,values=i)
    # import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data"," No Data found to Export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+  "Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport_table.focus()
        content=self.AttendanceReport_table.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_name.set(rows[1])
        self.var_attend_roll.set(rows[2])
        self.var_attend_time.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_status.set(rows[5])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_roll.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("")
    

    # Merge two CSV
    def mergeCsv(self):
        now=datetime.now()
        PATH='MergeAll'+now.strftime("%Y%m%d")+'.csv'
        files = os.listdir()
        line_count =0

        for file in files:
            print(file)
            if file.endswith('.csv'):
                with open(file,'r') as f1:
                    csv_reader = csv.reader(f1,delimiter=',')
                    with open('Merge_file/MergeAll'+now.strftime("%Y%m%d")+'.csv','a',newline='') as f2:
                        csv_writer =csv.writer(f2,delimiter=',')
                        if line_count==0:
                            csv_writer.writerow(['StudentId','Name','Roll','Time','Date','Status'])
                            line_count +=1
                        next(csv_reader,None)
                        for row in csv_reader:
                            #data=[file[:-4]] +row    #for index for filename
                            csv_writer.writerow(row)    
        messagebox.showinfo("Success","Merging of All CSV Files are completed",parent=self.root)  
               
    def csv_data_export_database(self):
        try:
            now=datetime.now()
            if len(mydata)<1:
                messagebox.showerror("No Data"," No Data found to Export", parent=self.root)
                return False
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            cursor=conn.cursor()
            with open('Merge_file/MergeAll'+now.strftime("%Y%m%d")+'.csv',newline='\n') as csv_file:
                csvfile = csv.reader(csv_file,delimiter=',')
                for row in csvfile:
                 query ='insert into attendance_details (studentId,name,roll,time,date,status) VALUES(%s,%s,%s,%s,%s,%s)'
                 cursor.execute(query,row)
                 print(row)
            conn.commit()
            conn.close()        
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)
    
    def data_import_database(self):
        try:
            now=datetime.now()
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            query='SELECT * FROM final_attendance_sheet;'
            results = pd.read_sql_query(query, conn)
            results.to_csv(r'Final_Attendance\final_attendance_sheet'+now.strftime("%Y%m%d")+'.csv', index=False)
            print(results)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

    def importCsv_FAS(self):
        global mydata_FAS
        mydata_FAS.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata_FAS.append(i)
            self.fetchData_FAS(mydata_FAS)    

        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 