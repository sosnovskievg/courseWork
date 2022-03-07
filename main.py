import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import mysql.connector
root =Tk()
root.title("Домашняя страница")
root.geometry("1080x650+100+20")
root.resizable(False, False) 
global root_window
is_admin = False
root_window = root
def on_closing():
    global is_on
    if is_admin:
        on_.config(image=off)
        is_on = False
    else:
        on_.config(image=on)
        is_on = True
    window.destroy()
def draw_login_page():
    global window
    newWindow = Toplevel(root_window)
    # newWindow.attributes('-alpha',0.9)
    newWindow.title("Авторизация")
    newWindow.geometry("400x400+500+200")
    newWindow.configure(bg="#fbb1bd")
    header=Frame(newWindow, bg="#23C3B8", bd=5)
    header.place(x=0,y=0,width=400,height=60)
    #heading label
    nsec = Label(header, text="База данных медиа файлов", font=("Helvetica", 18, "bold"), bg="orange", fg="#eae2b7")
    nsec.place(x=-10, y=10, width=420)
    username = Label(newWindow, text ="Логин", font=("Helvetica", 16), relief = FLAT, bg="#fbb1bd")
    username.place(x=20, y=100)
    username_input = Text(newWindow, height = 1,
                font = ("Helvetica", 16),
                width = 20,
                bg = "light yellow")
    username_input.place(x=120, y=100)
    password = Label(newWindow, text ="Пароль", font=("Helvetica", 16), relief = FLAT, bg="#fbb1bd")
    password.place(x=20, y=175)
    password_input = tkinter.Entry(newWindow,
                                   show = '*', 
                                   font = ("Helvetica", 16),
                                   width = 20,
                                   bg = "light yellow"
                                   )
    password_input.place(x=120, y=175)
    submit= Button(newWindow, text="Вход", command = login, font=("Helvetica", 16), bd =2, bg = "#e23946",fg="#eae2b7", relief=RAISED)
    submit.place(x=150, y=250, width = 100, height = 50)
    alert=Label(newWindow, text="По умолчанию: root/root",font=("Helvetica",8,), bg = "#23C3B8",fg="#eae2b7")
    alert.place(x=0, y=360, width=400)
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)
    window = newWindow
def login():
    username = window.winfo_children()[2].get(1.0, "end-1c")
    password = window.winfo_children()[4].get()
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    mycursor.execute("SELECT user_password FROM coursework.user_table WHERE  login= 'root'")
    rows = mycursor.fetchone()
    if rows == None:
        messagebox.showinfo("Ошибка",  "Что-то пошло не так")
        return
    server_pwd = rows[0]
    db.commit()
    db.close()
    # global is_on
    if username == "root" and password == server_pwd:
        tkinter.messagebox.showinfo("Успешно",  "Осуществлен вход")
        is_admin = True
        on_.config(image=off)
        is_on = False
        draw_admin()
    # else:
    #     tkinter.messagebox.showinfo("Failure",  "Access Denied")
    #     is_admin = False
    #     on_.config(image=on)
    #     is_on = True
    #     draw_visitor()
    window.destroy()
def button_mode():
   global is_on
   #Determine it is on or off
   if is_on:
      on_.config(image=off)
      is_on = False
      draw_login_page()
   else:
      on_.config(image = on)
      is_on = True
      is_admin = False
      draw_visitor()
      
def draw_search_authors():
    # import search_employee
    os.system('python search_authors.py')
def draw_search_student():
    # import search_student
    os.system('python search_users.py')
def draw_company_list():
    os.system('python view_1.py')
def draw_visitor_fees():
    os.system('python visitor_ganres.py')
def draw_notice_board():
    os.system('python view_titles.py')
def draw_edit_users():
    os.system('python edit_users.py')
def draw_edit_authors():
    os.system('python edit_authors.py')
def draw_edit_genres():
    os.system('python edit_genres.py')
def draw_edit_titles():
    os.system('python edit_titles.py')
def draw_change_password():
    os.system('python change_password.py')
def draw_execute_dbms():
    os.system('python execute_dbms.py')

def draw_visitor():
    for widget in dashboard.winfo_children():
        widget.destroy()
    welcome_text["text"] = "Добро пожаловать, гость"
    image1 = Image.open("media/justiceleague.jpg")
    test = ImageTk.PhotoImage(image1.resize((1080, 810), Image.ANTIALIAS))
    label1 = Label(dashboard,image=test)
    label1.photo = test
    label1.place(x=0, y=0, height = 400, width = 1080)
    option= Button(dashboard, text ="Поиск автора", command = draw_search_authors, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=150, y=75, width = 200, height = 50)
    option= Button(dashboard, text ="Поиск пользователя", command =  draw_search_student, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=730, y=75, width = 200, height = 50)
    option= Button(dashboard, text ="Жанры", command = draw_visitor_fees, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=150, y=275, width = 200, height = 50)
    option= Button(dashboard, text ="Список тайтлов", command = draw_notice_board,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=442, y=175, width = 200, height = 50)
    option= Button(dashboard, text ="Посты", command = draw_company_list,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=275, width = 200, height = 50)
def draw_admin():
    for widget in dashboard.winfo_children():
        widget.destroy()
    welcome_text["text"] = "Добро пожаловать, админстратор"
    image1 = Image.open("media/justiceleague.jpg")
    test = ImageTk.PhotoImage(image1.resize((1080, 810), Image.ANTIALIAS))
    label1 = Label(dashboard,image=test)
    label1.photo = test
    label1.place(x=0, y=0, height = 400, width = 1080)
    option= Button(dashboard, text ="Авторы", command = draw_edit_authors, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=100, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="Пользователи", command =  draw_edit_users, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="Смена пароль", command = draw_change_password, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=100, y=275, width = 250, height = 50)
    option= Button(dashboard, text ="Жанры", command = draw_edit_genres, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=420, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="Командная строка SQL", command = draw_execute_dbms, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=420, y=275, width = 250, height = 50)
    option= Button(dashboard, text ="Тайтлы", command = draw_edit_titles,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=275, width = 250, height = 50)
    
#Header
header=Frame(root, bg="#23C3B8", bd=0)
header.place(x=0,y=0,width=1080,height=115)
#logo
image1 = Image.open("media/кинопоисклого.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(header,image=test)
label1.image = test
label1.place(x=0, y=0, height = 120)
#heading label
nsec=Label(header, text="База данных медиа файлов",font=("Helvetica",36,"bold"), bg = "orange",fg="#eae2b7")
nsec.place(x=229, y=25, width=850)

#Profile frame
frame=Frame(root, bg="#fbb1bd")
frame.place(x=0,y=115,width=1080,height=50)
welcome_text = Label(frame, text = "Добро пожаловать, гость", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
is_on = True

# Define Our Images
on = PhotoImage(file ="media/on.png")
off = PhotoImage(file ="media/off.png")
# Create A Button
on_= Button(frame, image =on,bd =0, bg = "#fbb1bd", command = button_mode)
on_.place(x=950, y=0, width = 50, height = 50)
#visitor_text
visitor_text = Label(frame, text = "Гость", font=("Minion Pro Regular", 16), bg="#fbb1bd")
visitor_text.place(x=880, y=10)
#admin_text
admin_text = Label(frame, text = "Админ", font=("Minion Pro Regular", 16), bg="#fbb1bd")
admin_text.place(x=1000, y=10)
#profile picture
image1 = Image.open("media/profile.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(frame,image=test, bg = "#fbb1bd")
label1.place(x=820, y=0)

dashboard=Frame(root, bg="#bbb", bd=0)
dashboard.place(x=0,y=165,width=1080,height=400)
draw_visitor()
#Footer
footer=Frame(root, bg="#23C3B8", bd=0)
footer.place(x=0,y=565,width=1080,height=85)
root.mainloop()