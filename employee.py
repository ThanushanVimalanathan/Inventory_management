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
        return None,None
    
    return cursor,connection
    
connect_database()  
#---------------------------------------------------------------------------------------------------------#

#-------------------------------------Add Record----------------------------------------------------------# 

def treeview_data():
    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    cursor.execute('USE inventory_system')
    try:
       cursor.execute('SELECT * FROM employee_data')
       employee_records = cursor.fetchall()
       employee_treeview.delete(*employee_treeview.get_children())
    
       for record in employee_records:
           employee_treeview.insert('',END,values=record)
    
    except Exception as e:
        messagebox.showerror('Error',f'Error due to {e}')
    
    finally:
        cursor.close()
        connection.close()
        
        
#--------------------------------------clear Function-----------------------------------------------------------------------        
def clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry):
     empid_entry.delete(0,END) 
     name_entry.delete(0,END) 
     email_entry.delete(0,END) 
     gender_combobox.set('Select Gender') 
     
     from datetime import date
     dob_date_entry.set_date(date.today()) 
     contact_entry.delete(0,END) 
     employment_type_combobox.set('Select Type') 
     education_combobox.set('Select Gender') 
     work_shift_combobox.set('Select Shift') 
     address_text.delete("1.0", END)
     doj_date_entry.set_date(date.today()) 
     salary_entry.delete(0,END) 
     usertype_combobox.set('Select Type') 
     password_entry.delete(0,END)
     




 
def add_employee( empid,name,email,gender,dob,contact,education,employment_type,work_shift,address,doj,salary,usertype,password):
    if (empid == '' or name == '' or email == '' or gender == 'Select Gender' or contact == '' or employment_type == 'Select Type' or education == 'Select Education' or work_shift == 'Select Shift' or address == '\n' or salary == '' or usertype == 'Select User Type' or password == '' ):
         messagebox.showerror('Error','All fields are required')
         
    else:
        cursor,connection = connect_database() 
        if not cursor or not connection:
            return
        
        cursor.execute('USE inventory_system')
        
        try:
           cursor.execute('SELECT empid from employee_data WHERE empid=%s',(empid,))
           if cursor.fetchone():
               messagebox.showerror('Error','ID already exists')
           cursor.execute("""INSERT INTO employee_data (empid, name, email, gender, dob, contact,education,employment_type, work_shift, address,doj, salary, usertype, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(empid, name, email, gender, dob, contact,education,employment_type, work_shift, address,doj, salary, usertype, password))
           connection.commit()
           treeview_data()
           messagebox.showinfo('Success','Data is Inserted successfully')
        
        except Exception as e:
            messagebox.showerror('Error',f'Error due to {e}')
            
        finally:
           cursor.close()
           connection.close()
        


    
#--------------------------------------------------Database Creation-------------------------------------------------------#
def create_database_table():
    cursor,connection = connect_database()
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
    cursor.execute('USE inventory_system')
    cursor.execute('CREATE TABLE IF NOT EXISTS employee_data (empid INT(30) PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), gender VARCHAR(50),'
                   'dob VARCHAR(30),employment_type VARCHAR(50), contact VARCHAR(30) ,education varchar(50), work_shift VARCHAR(50), address VARCHAR(100), doj VARCHAR(30),'
                   'salary VARCHAR(50), usertype VARCHAR(50), password VARCHAR(50))')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   


#--------------------------------------------------Select Data--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
def select_data(event,empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,
                contact_entry,employment_type_combobox,education_combobox,work_shift_combobox,address_text,
                doj_date_entry,salary_entry,usertype_combobox,password_entry):
    
    clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,contact_entry,employment_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry)

    index = employee_treeview.selection()
    content = employee_treeview.item(index)
    row = content['values']
    
    empid_entry.insert(0,row[0])
    name_entry.insert(0,row[1])
    email_entry.insert(0,row[2])
    gender_combobox.set(row[3])
    dob_date_entry.set_date(row[4])
    contact_entry.insert(0,row[5])
    employment_type_combobox.set(row[6])
    education_combobox.set(row[7])
    work_shift_combobox.set(row[8])
    address_text.insert(1.0,row[9])
    doj_date_entry.set_date(row[10])
    salary_entry.insert(0,row[11])
    usertype_combobox.set(row[12])
    password_entry.insert(0,row[13])
    
    










#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 


def employee_form(window):
   global back_btn_img,employee_treeview
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
   employee_treeview = ttk.Treeview(topFrame,columns=('empid', 'name', 'email', 'gender', 'dob', 'contact','education','employment_type','work_shift', 'address','doj', 'salary', 'usertype', 'password'),show='headings',yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
   
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
   employee_treeview.heading('employment_type',text = 'Employee_Type')
   employee_treeview.heading('education',text = 'Education')
   
   employee_treeview.heading('work_shift',text = 'Work Shift')
   employee_treeview.heading('address',text = 'Emp_Address')
   employee_treeview.heading('doj',text = 'Date of Join')
   employee_treeview.heading('salary',text = 'Salary')
   employee_treeview.heading('usertype',text = 'user Type')
   employee_treeview.heading('password',text = 'Password')
   
   
   employee_treeview.column('empid',width=60)
   employee_treeview.column('name',width=140)
   employee_treeview.column('email',width=180)
   employee_treeview.column('gender',width=80)
   employee_treeview.column('dob',width=100)
   employee_treeview.column('contact',width=100)
   employee_treeview.column('employment_type',width=120)
   employee_treeview.column('education',width=120)
   
   employee_treeview.column('work_shift',width=100)
   employee_treeview.column('address',width=100)
   employee_treeview.column('doj',width=100)
   employee_treeview.column('salary',width=140)
   employee_treeview.column('usertype',width=120)
   employee_treeview.column('password',width=120)
   
   treeview_data()
   
    
   
   detail_frame = Frame(emp_frame,bg='light gray')
   detail_frame.place(x=20,y=300)
   
   
   #create id Label for data entry
   empid_label = Label(detail_frame,text='EmpId :',font=('times new roman',12))
   empid_label.grid(row=0,column=0,padx=20,pady=10,sticky='w')
   empid_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empid_entry.grid(row=0,column=1,padx=20,pady=10)
   
   #create name label for data entName
   name_label = Label(detail_frame,text='Name :',font=('times new roman',12))
   name_label.grid(row=0,column=2,padx=20,pady=10,sticky='w')
   name_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   name_entry.grid(row=0,column=3,padx=20,pady=10)
   
   #create name label for data Email
   email_label = Label(detail_frame,text='Email :',font=('times new roman',12))
   email_label.grid(row=0,column=4,padx=20,pady=10,sticky='w')
   email_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   email_entry.grid(row=0,column=5,padx=20,pady=10)
   
   #create name label for data Gender
   gender_label = Label(detail_frame,text='Gender :',font=('times new roman',12))
   gender_label.grid(row=1,column=0,padx=20,pady=10,sticky='w')
   gender_combobox = ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
   gender_combobox.set('Select Gender')
   gender_combobox.grid(row=1,column=1)
   
   #Dob Label
   dob_date_entry_label = Label(detail_frame,text='Date Of Birth :',font=('times new roman',12))
   dob_date_entry_label.grid(row=1,column=2,padx=20,pady=10,sticky='w')
   dob_date_entry = DateEntry(detail_frame,width=18, font=('times new roman',12),date_pattern='dd/mm/yyyy')
   dob_date_entry.grid(row=1,column=3) 
   
   #Contact Label
   contact_label = Label(detail_frame,text='Contact :',font=('times new roman',12))
   contact_label.grid(row=1,column=4,padx=20,pady=10,sticky='w')
   contact_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   contact_entry.grid(row=1,column=5,padx=20,pady=10)
   
   #Employee Type
   employment_type_label = Label(detail_frame,text='Employee Type :',font=('times new roman',12))
   employment_type_label.grid(row=2,column=0,padx=20,pady=10,sticky='w')
   employment_type_combobox = ttk.Combobox(detail_frame,values=('Full Time','Part Time','Casual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
   employment_type_combobox.set('Select Type')
   employment_type_combobox.grid(row=2,column=1)
   
   #Education
   education_label = Label(detail_frame,text='Education :',font=('times new roman',12))
   education_label.grid(row=2,column=2,padx=20,pady=10,sticky='w')
   
   education_option = ['B.Tech','M.Tech','B.Com','M.Com','Bsc','Msc','BBA','MBA','LLB','LLM','B.Arch','M.Arch']
   
   education_combobox = ttk.Combobox(detail_frame, values=education_option,font=('times new roman',12),width=18,state='readonly')
   education_combobox.set('Select Education')
   education_combobox.grid(row=2,column=3)
   
   
   #Work Shift
   work_shift_label = Label(detail_frame,text='Work Shift :',font=('times new roman',12))
   work_shift_label.grid(row=2,column=4,padx=20,pady=10,sticky='w')
   work_shift_combobox = ttk.Combobox(detail_frame,values=('Morning','Night'),font=('times new roman',12),width=18,state='readonly')
   work_shift_combobox.set('Select Shift')
   work_shift_combobox.grid(row=2,column=5)
   
   #Address Label
   address_label = Label(detail_frame,text='Address :',font=('times new roman',12))
   address_label.grid(row=3,column=0,padx=20,pady=10,sticky='w')
   address_text = Text(detail_frame,width=20,height=3,font=('times new roman',12),bg='light yellow')
   address_text.grid(row=3,column=1,rowspan=2)
   
   #date of join
   doj_label = Label(detail_frame,text='Date Of Joining :',font=('times new roman',12))
   doj_label.grid(row=3,column=2,padx=20,pady=10,sticky='w')
   doj_date_entry = DateEntry(detail_frame,width=18, font=('times new roman',12),date_pattern='dd/mm/yyyy')
   doj_date_entry.grid(row=3,column=3)
   
   #User Type Label
   usertype_label = Label(detail_frame,text='User Type :',font=('times new roman',12))
   usertype_label.grid(row=4,column=2,padx=20,pady=10,sticky='w')
   
   usertype_option = ['Admin','Employee']
   
   usertype_combobox = ttk.Combobox(detail_frame, values=usertype_option,font=('times new roman',12),width=18,state='readonly')
   usertype_combobox.set('Select User Type')
   usertype_combobox.grid(row=4,column=3)
   
   #salary Label
   salary_label = Label(detail_frame,text='Salary :',font=('times new roman',12))
   salary_label.grid(row=3,column=4,padx=20,pady=10,sticky='w')
   salary_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   salary_entry.grid(row=3,column=5,padx=20,pady=10)
   
   #Password Label
   password_label = Label(detail_frame,text='Password :',font=('times new roman',12))
   password_label.grid(row=4,column=4,padx=20,pady=10,sticky='w')
   password_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   password_entry.grid(row=4,column=5,padx=20,pady=10)
   
   #Button Frame
   button_frame = Frame(emp_frame,bg='white')
   button_frame.place(x=230,y=530)
   
   #Add button
   add_button = Button(button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d',
                       command= lambda : add_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_date_entry.get(),
                                            contact_entry.get(),employment_type_combobox.get(),education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),
                                            doj_date_entry.get(),salary_entry.get(),usertype_combobox.get(),password_entry.get()))
   
   add_button.grid(row=0,column=0,padx=20)
   
   #Remove button
   Update_button = Button(button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   Update_button.grid(row=0,column=1,padx=20)
   
   #Delete button
   Delete_button = Button(button_frame,text='Delete',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
   Delete_button.grid(row=0,column=2,padx=20)
   
   #Clear Button
   Clear_button = Button(button_frame,text='Clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda:clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,
                                                                                                                                                             contact_entry,employment_type_combobox,education_combobox,work_shift_combobox,address_text,
                                                                                                                                                             doj_date_entry,salary_entry,usertype_combobox,password_entry))
   Clear_button.grid(row=0,column=3,padx=20)
   employee_treeview.bind('<ButtonRelease-1>',lambda event:select_data(event,empid_entry,name_entry,email_entry,gender_combobox,dob_date_entry,
                                                          contact_entry,employment_type_combobox,education_combobox,work_shift_combobox,address_text,
                                                          doj_date_entry,salary_entry,usertype_combobox,password_entry))
   create_database_table()
   