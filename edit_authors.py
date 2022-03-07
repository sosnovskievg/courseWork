from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
import string
import random
root =Tk()
root.title("Поиск автора")
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
    mycursor = db.cursor()
    if search_input == "":
        mycursor.execute("SELECT * FROM coursework.authors")
    elif option == "Name":
        mycursor.execute("SELECT * FROM coursework.authors WHERE name = '" + str(search_input).upper() + "'")
    elif option == "UID":
        mycursor.execute("SELECT * FROM coursework.authors WHERE id = '" + str(search_input) + "'")
    else:
        return
    rows = mycursor.fetchall()
    data_table.delete(*data_table.get_children())
    if rows == None:
        note_text['text'] = "Data: 0 Rows"
        return
    note_text['text'] = "Data: "+str(len(rows))+" Rows"
    for row in rows:
        data_table.insert('', END, values=row)
    db.commit()
    db.close()
    # pass


# IT WILL SHOW VALUE FROM DATABASE
def show():
    id = IdEntry.get()
    name = NameEntry.get()
    bio = BioEntry.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM coursework.authors;")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        data_table.delete(*data_table.get_children())
    for row in rows:
        data_table.insert('', END, values=row)
    db.commit()
    db.close()

# IT WILL GET DATA IN LEFTBOX (getdata made events there and fecth value there also)
def getdata(event):
    currow = data_table.focus()
    contents = data_table.item(currow)
    row = contents['values']
    updatebt.configure(state = "normal")
    deletebt.configure(state = "normal")
    IdEntry.configure(state='normal')
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    BioEntry.delete(0, END)
    IdEntry.insert(0, row[0])
    IdEntry.configure(state='readonly')
    NameEntry.insert(0, row[1])
    BioEntry.insert(0, row[2])
    addbt.configure(state = 'disabled')

# IT WILL ADD DATAS
def add():

        iD=IdEntry.get()
        name=NameEntry.get()
        bio=BioEntry.get()
        db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
        mycursor=db.cursor()
        try:
           # mycursor.execute("INSERT INTO employee_table (id,name,desg,dept) VALUES ('"+str(iD)+"', '"+str(name).upper()+"', '"+str(desg).upper()+"', '"+str(dept).upper()+"')")
           mycursor.execute("INSERT INTO `coursework`.`authors`(`name`, `bio`) VALUES('"+str(name)+"', '"+str(bio).upper()+"')")
           db.commit()
           messagebox.showinfo("information","Record Inserted successfully")
           search()
           clear()
        except EXCEPTION as e:
           print(e)
           db.rollback()
           db.close()

def update():
    iD = IdEntry.get()
    name = NameEntry.get()
    bio=BioEntry.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    mycursor.execute("UPDATE coursework.authors SET name = '"+str(name) +"', bio = '" + str(bio) + "' where author_id = '"+str(iD)+"'")

    db.commit()
    messagebox.showinfo("Справка", "Запись изменена")
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    search()
    clear()

def delete1():
    iD = IdEntry.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    sql = "DELETE FROM coursework.authors WHERE author_id='"+str(iD)+"'"
    mycursor.execute(sql)
    db.commit()
    messagebox.showinfo("Справка", "Запись удалена")
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    search()
    clear()


# IT WILL CLEAR DATAS
def clear():
    updatebt.configure(state = "disabled")
    deletebt.configure(state = "disabled")
    IdEntry.configure(state='normal')
    IdEntry.delete(0, END)
    IdEntry.insert(0,random_string())
    NameEntry.delete(0, END)
    NameEntry.focus_set()
    addbt.configure(state='normal')

#Header
header=Frame(root, bg="brown", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec = Label(header, text="База данных медиа файлов", font=("Helvetica", 18, "bold"), bg="orange", fg="#eae2b7")
nsec.place(x=0, y=10, width=900)
#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Авторы", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text = "Закрыть", command = on_closing, bd = 0, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=820, y=0, height = 50, width = 80)
# LEFT BOX
leftbox=Frame(root,bd=0,bg="brown")
leftbox.place(x=10,y=140,width=300,height=350)

# INSIDE LEFT BOX
leftbox_title=Label(leftbox,text="Управление БД",font=("Helvetica",20,"bold"),fg="#eae2b7",bg="brown")
leftbox_title.place(x=30, y=10)
IdLabel=Label(leftbox,text="ID",font=("Helvetica",15),fg="#eae2b7",bg="brown")
IdLabel.place(x=10, y =50)
IdEntry=Entry(leftbox,font=("Helvetica",15),bd=0)
IdEntry.place(x=200, y =50, width = 80)
NameLabel=Label(leftbox,text="ФИО",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
NameLabel.place(x=10, y=100)
NameEntry=Entry(leftbox,font=("Helvetica", 15),bd=0)
NameEntry.place(x=80, y=100, width = 200)
DesignationLabel=Label(leftbox,text="Описание",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
DesignationLabel.place(x=10, y=150)
BioEntry=Entry(leftbox,font=("Helvetica", 15),bd=0)
BioEntry.place(x=130, y=150, width = 150)

# LEFT BOX BUTTONS
btnfrm=Frame(leftbox, bd=0, bg="brown")
btnfrm.place(x=10,y=250,width=290,height=50)

addbt=Button(btnfrm,text="Добавить",font=("Helvetica", 12),bg="indianred",fg="white",bd=0,command=add)
addbt.place(x=50, y=0, width = 70)
updatebt=Button(btnfrm,text="Изменить",font=("Helvetica", 12),bg="indianred",fg="white",bd=0,command=update)
updatebt.configure(state = "disabled")
updatebt.place(x=140, y=0, width = 70)

btnfrm2=Frame(leftbox,relief=RIDGE,bg="brown")
btnfrm2.place(x=10,y=300,width=290,height=50)

deletebt=Button(btnfrm2,text="Удалить",font=("Helvetica", 12),bg="indianred",fg="white",command=delete1, bd =0)
deletebt.configure(state = "disabled")
deletebt.place(x=50, y=0, width = 70)
clrbt=Button(btnfrm2,text="Очистить",font=("Helvetica", 12),bg="indianred",fg="white",command=clear, bd = 0)
clrbt.place(x=140, y=0, width = 70)






# RIGHT BOX
rightbox=Frame(root,bd=0,bg="indianred")
rightbox.place(x=320,y=140,width=570,height=350)

# RIGHT BOX HEADING
searchBy=Label(rightbox,text="Введите значение",font=("Helvetica", 10),bg="indianred",fg="white")
searchBy.place(x=10, y=10)
searchInput=Entry(rightbox,font=("Helvetica", 12),bd=0,width=17)
searchInput.place(x=130, y=10, height = 30)
dropdown=ttk.Combobox(rightbox,font=("Helvetica",12),state='readonly', width = 12)
dropdown['values']=("--поиск по--", "Имени", "ID")
dropdown.current(0)
dropdown.place(x=300, y=10, height = 30)
searchBtn=Button(rightbox,text="Поиск",command=search,font=("Helvetica", 12),width=10, bd = 0)
searchBtn.place(x=450, y=10, height = 30)

# BOX INSIDE RIGHT BOX
tabfrm=Frame(rightbox,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=50,width=550,height=270)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
data_table=ttk.Treeview(tabfrm,columns=("author_id","name","Bio"),yscrollcommand=scrolly.set)
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=data_table.yview)

note_text=Label(rightbox,font=("Helvetica", 10),bg="indianred",fg="white")
note_text.place(x=10, y=325)

# INSIDE RIGHT BOX
data_table.heading("author_id",text="ID")
data_table.heading("name",text="Name")
data_table.heading("Bio",text="Designation")

data_table['show']="headings"
data_table.column("author_id",width = 10)
data_table.column("name",width=200)
data_table.column("Bio",width=30)
data_table.pack(fill=BOTH,expand=1)
data_table.bind("<ButtonRelease-1>",getdata)
search()



root.mainloop()