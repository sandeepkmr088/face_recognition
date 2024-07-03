from tkinter import *
import tkinter as tk    #import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from csv import DictWriter
import os 
from time import strftime
import datetime
from datetime import datetime
import datetime as dt




class Form:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")   # layout for Screen
        self.root.title("Sample Data Information")   # title of page


        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # student current Information Frame
        current_course_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Location Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=400,y=0, width=800,height=90)

        # state
        dep_label=Label(current_course_frame,text="State Name",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select State Name","Assam","West Bengal","Arunachal Pradesh","Sikkim")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)


        # City
        course_label=Label(current_course_frame,text="City Name",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select City Name ","Dibrugarh","Kolkata","Arunachal Pradesh","Gangtok","Guwahati")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        # Center Name
        year_label=Label(current_course_frame,text="Center Name",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Center Name","CName-01","CName-02","Cname-03","CName-04","CName-05")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)

         # Sample Type
        semester_label=Label(current_course_frame,text="Sample Type",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Type ","raw fish","raw milk","raw food","raw vegetables","raw meat","raw chicken")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)


        #  Information Frame
        class_Student_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Sample Details Informations", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=400,y=100, width=800,height=420)
        now=datetime.now()
        #Date
        studentId_label=Label(class_Student_frame,text="Date Time",font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        studentID_entry=Label(class_Student_frame,text=now.strftime("%d-%m-%Y  %H:%M:%S %p"),width=20,font=("times new roman",12,"bold"),bg="black",fg="white")
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Person Name
        studentName_label=Label(class_Student_frame,text="Person Name",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Shop Number
        class_div_label=Label(class_Student_frame,text="Shop Number",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        class_div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

                
        # Sample Weight
        rool_no_label=Label(class_Student_frame,text="Sample Weight",font=("times new roman",12,"bold"))
        rool_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        rool_no_entry=ttk.Combobox(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rool_no_entry["values"]=("Select Weight","50g","100g","150g","200g","250g","300g")
        rool_no_entry.current(0)
        rool_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # GEnder
        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Select Gender","Female","Male")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        # address
        DOB_label=Label(class_Student_frame,text="Address",font=("times new roman",12,"bold"))
        DOB_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        DOB_entry=Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)

        # Email
        email_label=Label(class_Student_frame,text="Email",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        email_entry=Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=10,sticky=W)

        # Phone No
        phone_label=Label(class_Student_frame,text="Phone",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        phone_entry=Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=10,sticky=W)

        # Sample Collector Name
        address_label=Label(class_Student_frame,text="Collector Name",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        address_entry=Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=10,sticky=W)

        # COllector ID
        teacher_label=Label(class_Student_frame,text="Collector ID",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        teacher_entry=Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=5,pady=10,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Yes, handwashing facilities in the market", value="Yes", )
        radionbtn1.grid(row=5,column=0)

        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No, handwashing facilities in the market", value="No")
        radionbtn2.grid(row=5,column=1)

        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Yes, market is cleaned regularly", value="Yes", )
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No, market is not cleaned regularly", value="No")
        radionbtn2.grid(row=6,column=1)

        #button Frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=758,height=50)

        save_btn=Button(btn_frame,text="Save",width=18,font=("times new roman",13,"bold"),bg="#033e6b",fg="white",activeforeground="white",activebackground="#033e6b")
        save_btn.grid(row=0,column=0,pady=5)

        update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="#033e6b",fg="white",activeforeground="white",activebackground="#033e6b")
        update_btn.grid(row=0,column=1,pady=5)

        delete_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",13,"bold"),bg="#033e6b",fg="white",activeforeground="white",activebackground="#033e6b")
        delete_btn.grid(row=0,column=3,pady=5)

        reset_btn=Button(btn_frame,text="Reset",width=18,font=("times new roman",13,"bold"),bg="#033e6b",fg="white",activeforeground="white",activebackground="#033e6b")
        reset_btn.grid(row=0,column=4,pady=5)

        #Create button code action function
        def action():
           
            #username = name_var.get()
           # userage = age_var.get()
            #useremail = email_var.get()
           # usermobile = mobile_var.get()
           # usergender = gender_var.get()
            #usertype = user_type.get()
            #change value 0,1 to Yes or No
           # if checkbtn_var.get() == 0:
          #      subscribe = 'No'
           # else:
           #     subscribe = 'Yes'

            #write to csv file code here
            with open('file.csv', 'a', newline = '') as f:
                dict_writer = DictWriter(f, fieldnames=['User Name', 'User Age', 'User Email','User Mobile', 'User Gender', 'User Type', 'Subscribe'])
                if os.stat('file.csv').st_size == 0:        #if file is not empty than header write else not
                    dict_writer.writeheader()
            
                dict_writer.writerow({
                    
                 #   'User Name' : username,
                 #   'User Age' : userage,
                 #   'User Email' : useremail,
                 #   'User Mobile' : usermobile,
                  #  'User Gender' : usergender,
                  #  'User Type' : usertype,
                  #  'Subscribe' : subscribe
                })
            #Change color after submit button
           
          #  name_entrybox.delete(0, tk.END)
           # age_entrybox.delete(0, tk.END)
           # email_entrybox.delete(0, tk.END)
          #  mobile_entrybox.delete(0, tk.END)
          #  name_label.configure(foreground = 'Blue')
           # email_label.configure(foreground = 'Blue')
           # age_label.configure(foreground = 'Blue')
          #  mobile_label.configure(foreground = 'Blue')
         #   gender_label.configure(foreground = 'Blue')

        #submit button
       # submit_button = ttk.Button(self.root, text = "Submit", command = action)  
      #  submit_button.grid(row=7, column=0)
        

if __name__ == "__main__":
    root=Tk()
    obj=Form(root)
    root.mainloop()  