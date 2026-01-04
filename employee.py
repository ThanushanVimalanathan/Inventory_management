from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import pymysql


#-----------------------------------DataBase Connection----------------------------------------#
def connect_database():
    try:
       connection = pymysql.connect(host='localhost',user='root',password = '1234')
       cursor = connection.cursor()
    except:
        messagebox.showerror('Error','Database connectivity error')
        return 
    
    
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
    cursor.execute('USE inventory_systemn')
    cursor.execute('CREATE TABLE IF NOT EXISTS employee_data (empid INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), gender VARCHAR(50),'
                   'dob VARCHAR(30), contact VARCHAR(30), employment_type VARCHAR(50), work_shift VARCHAR(50), address VARCHAR(100), doj VARCHAR(30),'
                   'salary VARCHAR(50), usertype VARCHAR(50), password VARCHAR(50))')
    
    
#---------------------------------------------------------------------------------------------------------#
   

def employee_form(window):
   global back_btn_img
   emp_frame = Frame(
       window,
       width=1070,
       height=567,
       bg='white'
    ) 
   emp_frame.place(x=200,y=100)
   headingLabel = Label(emp_frame,text='Employee Details Controller', font=('times new roman',16,'bold'),bg="#060647",fg='white')
   headingLabel.place(x=0,y=0,relwidth=1)
   
   back = Image.open('assets/back_button.png')
   back = back.resize((34, 34), Image.LANCZOS)
   back_btn_img = ImageTk.PhotoImage(back)
   
   back_button = Button(
       emp_frame,
       image=back_btn_img,
       bd=0,
       cursor='hand2',
       bg='white',
       command=lambda:emp_frame.place_forget()
    )
   back_button.place(x=10,y=30)
   
   topFrame = Frame(emp_frame,bg='white')
   topFrame.place(x=0,y=65,relwidth=1,height=235)
   search_frame = Frame(topFrame,bg='white')
   search_frame.pack()
   
   search_combobox = ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12),state='readonly')
   search_combobox.set('Search by')
   search_combobox.grid(row=0,column=0,padx=20)
   
   search_entry = Entry(search_frame,font=('times new roman',12),bg='lightyellow')
   search_entry.grid(row=0,column=1)
   
   search_button = Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   search_button.grid(row=0,column=2,padx=20)
   
   showAll_button = Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   showAll_button.grid(row=0,column=3)
   
   horizontal_scrollbar = Scrollbar(topFrame,orient=HORIZONTAL)
   vertical_scrollbar = Scrollbar(topFrame,orient=VERTICAL)
   employee_treeview = ttk.Treeview(topFrame,columns=('empid','name','email','gender','dob','contact','employement_type','education','work_shift','address','doj','salary','usertype'),show='headings',yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
   
   horizontal_scrollbar.pack(side=BOTTOM,fill=X)
   vertical_scrollbar.pack(side=RIGHT,fill=Y,pady=(10,0))
   
   horizontal_scrollbar.config(command=employee_treeview.xview)
   vertical_scrollbar.config(command=employee_treeview.yview)
   employee_treeview.pack(pady=(10,0))
   
   employee_treeview.heading('empid',text = 'EmpID')
   employee_treeview.heading('name',text = 'Name')
   employee_treeview.heading('email',text = 'E-Mail')
   employee_treeview.heading('gender',text = 'Gender')
   employee_treeview.heading('dob',text = 'Date Of Birth')
   employee_treeview.heading('contact',text = 'Contact')
   employee_treeview.heading('employement_type',text = 'Employee_Type')
   employee_treeview.heading('education',text = 'Education')
   employee_treeview.heading('work_shift',text = 'Work Shift')
   employee_treeview.heading('address',text = 'Emp_Address')
   employee_treeview.heading('doj',text = 'Date of Join')
   employee_treeview.heading('salary',text = 'Salary')
   employee_treeview.heading('usertype',text = 'user Type')
   
   employee_treeview.column('empid',width=60)
   employee_treeview.column('name',width=140)
   employee_treeview.column('email',width=180)
   employee_treeview.column('gender',width=80)
   employee_treeview.column('dob',width=100)
   employee_treeview.column('contact',width=100)
   employee_treeview.column('employement_type',width=120)
   employee_treeview.column('education',width=120)
   employee_treeview.column('work_shift',width=100)
   employee_treeview.column('address',width=100)
   employee_treeview.column('doj',width=100)
   employee_treeview.column('salary',width=140)
   employee_treeview.column('usertype',width=120)
   
   detail_frame = Frame(emp_frame,bg='light gray')
   detail_frame.place(x=20,y=300)
   
   #create id Label for data entry
   empId_label = Label(detail_frame,text='EmpId :',font=('times new roman',12))
   empId_label.grid(row=0,column=0,padx=20,pady=10,sticky='w')
   empId_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empId_entry.grid(row=0,column=1,padx=20,pady=10)
   
   #create name label for data entName
   empName_label = Label(detail_frame,text='Name :',font=('times new roman',12))
   empName_label.grid(row=0,column=2,padx=20,pady=10,sticky='w')
   empName_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empName_entry.grid(row=0,column=3,padx=20,pady=10)
   
   #create name label for data Email
   empEmail_label = Label(detail_frame,text='Email :',font=('times new roman',12))
   empEmail_label.grid(row=0,column=4,padx=20,pady=10,sticky='w')
   empEmail_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empEmail_entry.grid(row=0,column=5,padx=20,pady=10)
   
   #create name label for data Gender
   gender_label = Label(detail_frame,text='Gender :',font=('times new roman',12))
   gender_label.grid(row=1,column=0,padx=20,pady=10,sticky='w')
   gender_combobox = ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
   gender_combobox.set('Select Gender')
   gender_combobox.grid(row=1,column=1)
   
   #Dob Label
   Dob_label = Label(detail_frame,text='Date Of Birth :',font=('times new roman',12))
   Dob_label.grid(row=1,column=2,padx=20,pady=10,sticky='w')
   Dob_date_entry = DateEntry(detail_frame,width=18, font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
   Dob_date_entry.grid(row=1,column=3) 
   
   #Contact Label
   contact_label = Label(detail_frame,text='Contact :',font=('times new roman',12))
   contact_label.grid(row=1,column=4,padx=20,pady=10,sticky='w')
   contact_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   contact_entry.grid(row=1,column=5,padx=20,pady=10)
   
   #Employee Type
   Emp_label = Label(detail_frame,text='Employee Type :',font=('times new roman',12))
   Emp_label.grid(row=2,column=0,padx=20,pady=10,sticky='w')
   Emp_combobox = ttk.Combobox(detail_frame,values=('Full Time','Part Time','Casual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
   Emp_combobox.set('Select Type')
   Emp_combobox.grid(row=2,column=1)
   
   #Education
   Education_label = Label(detail_frame,text='Education :',font=('times new roman',12))
   Education_label.grid(row=2,column=2,padx=20,pady=10,sticky='w')
   
   education_option = ['B.Tech','M.Tech','B.Com','M.Com','Bsc','Msc','BBA','MBA','LLB','LLM','B.Arch','M.Arch']
   
   Education_combobox = ttk.Combobox(detail_frame, values=education_option,font=('times new roman',12),width=18,state='readonly')
   Education_combobox.set('Select Education')
   Education_combobox.grid(row=2,column=3)
   
   
   #Work Shift
   WorkShift_label = Label(detail_frame,text='Employee Type :',font=('times new roman',12))
   WorkShift_label.grid(row=2,column=4,padx=20,pady=10,sticky='w')
   WorkShift_combobox = ttk.Combobox(detail_frame,values=('Morning','Night'),font=('times new roman',12),width=18,state='readonly')
   WorkShift_combobox.set('Select Shift')
   WorkShift_combobox.grid(row=2,column=5)
   
   #Address Label
   Address_label = Label(detail_frame,text='Address :',font=('times new roman',12))
   Address_label.grid(row=3,column=0,padx=20,pady=10,sticky='w')
   Address_text = Text(detail_frame,width=20,height=3,font=('times new roman',12),bg='light yellow')
   Address_text.grid(row=3,column=1,rowspan=2)
   
   #date of join
   Doj_label = Label(detail_frame,text='Date Of Joining :',font=('times new roman',12))
   Doj_label.grid(row=3,column=2,padx=20,pady=10,sticky='w')
   Doj_date_entry = DateEntry(detail_frame,width=18, font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
   Doj_date_entry.grid(row=3,column=3)
   
   #User Type Label
   Education_label = Label(detail_frame,text='User Type :',font=('times new roman',12))
   Education_label.grid(row=4,column=2,padx=20,pady=10,sticky='w')
   
   Education_option = ['Admin','Employee']
   
   Education_combobox = ttk.Combobox(detail_frame, values=Education_option,font=('times new roman',12),width=18,state='readonly')
   Education_combobox.set('Select User Type')
   Education_combobox.grid(row=4,column=3)
   
   #salary Label
   Salary_label = Label(detail_frame,text='Salary :',font=('times new roman',12))
   Salary_label.grid(row=3,column=4,padx=20,pady=10,sticky='w')
   Salary_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   Salary_entry.grid(row=3,column=5,padx=20,pady=10)
   
   #Password Label
   Password_label = Label(detail_frame,text='Password :',font=('times new roman',12))
   Password_label.grid(row=4,column=4,padx=20,pady=10,sticky='w')
   Password_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   Password_entry.grid(row=4,column=5,padx=20,pady=10)
   
   #Button Frame
   button_frame = Frame(emp_frame,bg='white')
   button_frame.place(x=230,y=530)
   
   add_button = Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   add_button.grid(row=0,column=0,padx=20)
   
   #Remove button
   Update_button = Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   Update_button.grid(row=0,column=1,padx=20)
   
   #Delete button
   Delete_button = Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   Delete_button.grid(row=0,column=2,padx=20)
   
   #Clear Button
   Clear_button = Button(button_frame,text='Clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   Clear_button.grid(row=0,column=3,padx=20)
   