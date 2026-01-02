from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry


#----------------------------------Functionality Part--------------------------------------------------#
def employee_form():
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
   
   detail_frame = Frame(emp_frame)
   detail_frame.place(x=0,y=300)
   
   #create id Label for data entry
   empId_label = Label(detail_frame,text='EmpId:',font=('times new roman',12))
   empId_label.grid(row=0,column=0)
   empId_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empId_entry.grid(row=0,column=1,padx=20,pady=10)
   
   #create name label for data entName
   empName_label = Label(detail_frame,text='Name:',font=('times new roman',12))
   empName_label.grid(row=0,column=2)
   empName_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empName_entry.grid(row=0,column=3,padx=20,pady=10)
   
   #create name label for data entEmail
   empEmail_label = Label(detail_frame,text='Email:',font=('times new roman',12))
   empEmail_label.grid(row=0,column=6)
   empEmail_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   empEmail_entry.grid(row=0,column=7,padx=20,pady=10)
   
   #create name label for data Gender
   gender_label = Label(detail_frame,text='Gender',font=('times new roman',12))
   gender_label.grid(row=1,column=0,padx=20,pady=10)
   gender_combobox = ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
   gender_combobox.set('Select Gender')
   gender_combobox.grid(row=1,column=1)
   
   #Dob Label
   gender_label = Label(detail_frame,text='Date Of Birth',font=('times new roman',12))
   gender_label.grid(row=1,column=2,padx=20,pady=10)
   
   Dob_date_entry = DateEntry(detail_frame,width=18, font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
   Dob_date_entry.grid(row=1,column=3) 
   
   #Contact Label
   contact_label = Label(detail_frame,text='Contact:',font=('times new roman',12))
   contact_label.grid(row=1,column=4,padx=20,pady=10)
   contact_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
   contact_entry.grid(row=1,column=1,padx=20,pady=10)
   
   
   




#------------------------------------GUI Part-----------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
window = Tk()
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='gray')

img = Image.open('assets/inventory.png')
img = img.resize((64, 64), Image.LANCZOS)
bgImg = ImageTk.PhotoImage(img)

titleLabel = Label(
    
    window,
    image=bgImg,
    compound=LEFT,
    text='  Inventory Management System',
    font=('times new roman', 40, 'bold'),
    bg="#b74009",
    fg='white',
    anchor='w',
    padx=20
)
titleLabel.place(x=0, y=0,relwidth=1)#relwidth for asign center for allocate with 1

logoutButton = Button(window,text='Logout',font=('time new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100,y=10)#place logout Button

#subLabel
subtitleLabel = Label(
    window,
    text='Welcome Admin\t\t Date: 08-07-2025\t\t Time: 12:40:17 pm',
    font=('times new roman',15),
    bg='#4d636d'
)
subtitleLabel.place(x=0,y=70,relwidth=1)


#Create Sidebar
leftFrame = Frame(window)
leftFrame.place(x=0,y=100,width=200,height=500)


LogoImg = Image.open('assets/checklist.png')
LogoImg = LogoImg.resize((150, 150), Image.LANCZOS)
Logo = ImageTk.PhotoImage(LogoImg)

ImageLabel = Label(leftFrame,image=Logo)
ImageLabel.pack()


#Create Menu Label
menuLabel = Label(
    leftFrame, 
    text='Menu',
    font=('time new roman', 20),
    bg='#009688'
)

#Employee Button and Icon
EmpImg = Image.open('assets/employee.png')
EmpImg = EmpImg.resize((40, 40), Image.LANCZOS)
Emp = ImageTk.PhotoImage(EmpImg)

menuLabel.pack(fill=X)
empoloyee_button = Button(
    leftFrame,
    image=Emp,
    compound=LEFT,
    text='Employees',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10,
    command=employee_form
    
)
empoloyee_button.pack(fill=X)

#Create Supplier button
SupImg = Image.open('assets/supplier.png')
SupImg = SupImg.resize((40, 40), Image.LANCZOS)
Sup = ImageTk.PhotoImage(SupImg)

menuLabel.pack(fill=X)
supplier_Button = Button(
    leftFrame,
    image=Sup,
    compound=LEFT,
    text='Supplier',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10
    
)
supplier_Button.pack(fill=X)


#Create Category
CatImg = Image.open('assets/category.png')
CatImg = CatImg.resize((40, 40), Image.LANCZOS)
Cat = ImageTk.PhotoImage(CatImg)

menuLabel.pack(fill=X)
Cat_button = Button(
    leftFrame,
    image=Cat,
    compound=LEFT,
    text='Category',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10
    
)
Cat_button.pack(fill=X)

#Product
ProImg = Image.open('assets/box.png')
ProImg = ProImg.resize((40, 40), Image.LANCZOS)
Pro = ImageTk.PhotoImage(ProImg)

menuLabel.pack(fill=X)
product_button = Button(
    leftFrame,
    image=Pro,
    compound=LEFT,
    text='Product',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10
    
)
product_button.pack(fill=X)

#Sales
SalImg = Image.open('assets/sales.png')
SalImg = SalImg.resize((40, 40), Image.LANCZOS)
Sal = ImageTk.PhotoImage(SalImg)

menuLabel.pack(fill=X)
sales_button = Button(
    leftFrame,
    image=Sal,
    compound=LEFT,
    text='Sales',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10
    
)
sales_button.pack(fill=X)

#Exit
ExtImg = Image.open('assets/logout.png')
ExtImg = ExtImg.resize((40, 40), Image.LANCZOS)
Ext = ImageTk.PhotoImage(ExtImg)

menuLabel.pack(fill=X)
exit_button = Button(
    leftFrame,
    image=Ext,
    compound=LEFT,
    text='Exit',
    font=('times new roman',20,'bold'),
    anchor='w',
    padx=10
    
)
exit_button.pack(fill=X)



#-----------------------------------------employee frame card---------------------------------------------------------------
emp_frame = Frame(
    window,
    bg='#2C3E50',
    bd=3,
    relief=RIDGE
)
emp_frame.place(x=400, y=125, height=150, width=250)

total_emp_icon = Image.open('assets/businessman.png')
total_emp_icon = total_emp_icon.resize((50, 50), Image.LANCZOS)
total_emp = ImageTk.PhotoImage(total_emp_icon)


total_emp_icon_label = Label(emp_frame, image=total_emp,bg='#2C3E50')
total_emp_icon_label.pack()

total_emp_label = Label(emp_frame,text='Total Employee',bg='#2C3E50',fg='white',font=('times new roman',25,'bold'))
total_emp_label.pack()

total_emp_count_label = Label(emp_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()

#---------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------Supplier frame card---------------------------------------------------------------

sup_frame = Frame(
    window,
    bg="#241580",
    bd=3,
    relief=RIDGE
)
sup_frame.place(x=800, y=125, height=150, width=250)

total_sup_icon = Image.open('assets/supply.png')
total_sup_icon = total_sup_icon.resize((50, 50), Image.LANCZOS)
total_sup = ImageTk.PhotoImage(total_sup_icon)


total_sup_icon_label = Label(sup_frame, image=total_sup,bg='#241580')
total_sup_icon_label.pack()

total_sup_label = Label(sup_frame,text='Total Supplier',bg='#241580',fg='white',font=('times new roman',25,'bold'))
total_sup_label.pack()

total_sup_count_label = Label(sup_frame,text='12',bg='#241580',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.pack()

#---------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------Categeory frame card---------------------------------------------------------------

cat_frame = Frame(
    window,
    bg="#098074",
    bd=3,
    relief=RIDGE
)
cat_frame.place(x=400, y=310, height=150, width=250)

total_cat_icon = Image.open('assets/widget.png')
total_cat_icon = total_cat_icon.resize((50, 50), Image.LANCZOS)
total_cat = ImageTk.PhotoImage(total_cat_icon)


total_cat_icon_label = Label(cat_frame, image=total_cat,bg='#098074')
total_cat_icon_label.pack()

total_cat_label = Label(cat_frame,text='Total Categeory',bg='#098074',fg='white',font=('times new roman',25,'bold'))
total_cat_label.pack()

total_cat_count_label = Label(cat_frame,text='12',bg='#098074',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()

#---------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------Supplier frame card---------------------------------------------------------------

pro_frame = Frame(
    window,
    bg="#3C3A48",
    bd=3,
    relief=RIDGE
)
pro_frame.place(x=800, y=310, height=150, width=250)

total_pro_icon = Image.open('assets/gross.png')
total_pro_icon = total_pro_icon.resize((50, 50), Image.LANCZOS)
total_pro = ImageTk.PhotoImage(total_pro_icon)


total_pro_icon_label = Label(pro_frame, image=total_pro,bg="#3C3A48")
total_pro_icon_label.pack()

total_pro_label = Label(pro_frame,text='Total Product',bg='#3C3A48',fg='white',font=('times new roman',25,'bold'))
total_pro_label.pack()

total_pro_count_label = Label(pro_frame,text='12',bg='#3C3A48',fg='white',font=('times new roman',30,'bold'))
total_pro_count_label.pack()

#---------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------Sales frame card---------------------------------------------------------------

sal_frame = Frame(
    window,
    bg="#570F38",
    bd=3,
    relief=RIDGE
)
sal_frame.place(x=600, y=495, height=150, width=250)

total_sal_icon = Image.open('assets/trend.png')
total_sal_icon = total_sal_icon.resize((50, 50), Image.LANCZOS)
total_sal = ImageTk.PhotoImage(total_sal_icon)


total_sal_icon_label = Label(sal_frame, image=total_sal,bg='#570F38')
total_sal_icon_label.pack()

total_sal_label = Label(sal_frame,text='Total Categeory',bg='#570F38',fg='white',font=('times new roman',25,'bold'))
total_sal_label.pack()

total_sal_count_label = Label(sal_frame,text='12',bg='#570F38',fg='white',font=('times new roman',30,'bold'))
total_sal_count_label.pack()

#---------------------------------------------------------------------------------------------------------------------#

window.mainloop()
