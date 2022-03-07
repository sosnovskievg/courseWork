import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
root =Tk()
root.title("Поиск пользователя")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root
def on_closing():
    root_window.destroy()

def search():
    option = dropdown.get()
    search_input = searchInput.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor(buffered = True)
    if option == "Логин":
        mycursor.execute("SELECT * FROM coursework.user_table WHERE login = '" + str(search_input) + "'")
    elif option == "Id":
        mycursor.execute("SELECT * FROM coursework.user_table WHERE user_id = '" + str(search_input) + "'")
    else:
        return
    rows = mycursor.fetchone()
    if rows == None:
        draw_no_result()
        return
    draw_result()
    global result, result_uid, result_name, result_role
    result_uid["text"] = rows[0]
    result_name["text"] = rows[1]
    result_role["text"] =  rows[3]

    db.commit()
    db.close()
    # pass 
def draw_result():
    #result_frame
    global result, result_uid, result_name, result_role
    for widget in result.winfo_children():
        widget.destroy()
    result=Frame(root, bg = "#777", bd=0)
    result.place(x=100,y=200,width=700,height=250)
    name=Label(result, text = "Логин : ", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    name.place(x=100, y=60, height = 30)
    result_name=Label(result, text = "undefined", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    result_name.place(x=270, y=60, height = 30)
    uid=Label(result, text = "Id : ", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    uid.place(x=100, y=90, height = 30)
    result_uid=Label(result, text = "undefined", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    result_uid.place(x=270, y=90, height = 30)
    dept=Label(result, text = "Роль : ", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    dept.place(x=100, y=120, height = 30)
    result_role=Label(result, text = "undefined", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    result_role.place(x=270, y=120, height = 30)
def draw_no_result():
    #result_frame
    global result
    for widget in result.winfo_children():
        widget.destroy()     
    result=Frame(root, bg = "#777", bd=0)
    result.place(x=100,y=200,width=700,height=250)
    name=Label(result, text = "No record found", font=("Minion Pro Regular",20), bd = 0, bg = "#777", fg = "#fff")
    name.place(x=0, y=100, height = 30, width = 700)
#Header
header=Frame(root, bg="#23C3B8", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec = Label(header, text="База данных медиа файлов", font=("Helvetica", 18, "bold"), bg="orange", fg="#eae2b7")
nsec.place(x=0, y=20, width=900)

#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Поиск по Id/логину", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)

close = Button(frame2, text = "Выход", bd = 0, command = on_closing, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)

#panel
panel=Frame(root, bg="#bbb", bd=0)
panel.place(x=0,y=125,width=900,height=375)
#panel_elements
searchBy=Label(panel,text="Введите значение",font=("Minion Pro Regular",16),bg="#bbb",fg="#222")
searchBy.place(x=40, y=20)
searchInput=Entry(panel,font=("Minion Pro Regular",12), bd = 0)
searchInput.place(x=230, y=20, height = 30, width = 220)
dropdown=ttk.Combobox(panel, width=15, font=("Minion Pro Regular",16), state='readonly')
dropdown['values']=("--поиск по--", "Логин", "Id")
dropdown.current(0)
dropdown.place(x=480, y=20, height = 30)
searchBtn=Button(panel,text="Искать", command = search, font=("Minion Pro Regular",16,"bold"), bd = 0)
searchBtn.place(x=700, y=20, height = 30)

result=Frame(root, bd=0)
result.place(x=0,y=0,width=0,height=0)

root.mainloop()