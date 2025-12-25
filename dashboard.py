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


window.mainloop()
