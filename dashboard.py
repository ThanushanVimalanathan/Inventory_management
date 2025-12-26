from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

img = Image.open('assets/inventory.png')
img = img.resize((64, 64), Image.LANCZOS)
bgImg = ImageTk.PhotoImage(img)

titleLabel = Label(
    
    window,
    image=bgImg,
    compound=LEFT,
    text='  Inventory Management System',
    font=('times new roman', 40, 'bold'),
    bg='#010c48',
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
    text='Wlcom Admin\t\t Date: 08-07-2025\t\t Time: 12:40:17 pm',
    font=('times new roman',15),
    bg='#4d636d'
)
subtitleLabel.place(x=0,y=70,relwidth=1)


#Create Sidebar
leftFrame = Frame(window)
leftFrame.place(x=0,y=102,width=200,height=500)


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
    padx=10
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




window.mainloop()
