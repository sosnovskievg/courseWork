from tkinter import*
import mysql.connector
from tkinter import ttk, messagebox
root =Tk()
root.title("Список тайтлов")
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
        mycursor.execute("SELECT * FROM coursework.titles;")
    elif option == "Name":
        mycursor.execute("SSELECT * FROM coursework.titles WHERE name = '" + str(search_input).upper() + "'")
    elif option == "Year":
        mycursor.execute("SELECT * FROM company_list WHERE year genre_id = '" + str(search_input).upper() + "'")

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



def getdata(event):
    currow = data_table.focus()
    contents = data_table.item(currow)
    row = contents['values']
    updatebt.configure(state = "normal")
    deletebt.configure(state = "normal")
    idEntry.configure(state='normal')
    idEntry.delete(0, END)
    MarkEntry.delete("1.0", "end")
    nameEntry.delete("1.0", "end")
    descEntry.delete("1.0", "end")
    idEntry.insert(0, row[1])
    idEntry.configure(state='readonly')
    nameEntry.insert(END, row[2])
    descEntry.insert(END, row[3])
    addbt.configure(state = 'disabled')
    MarkEntry.insert(END, row[5])
    MarkEntry.configure(state='normal')



def add():

        id=idEntry.get()
        name = nameEntry.get(1.0,"end-1c")
        desc=descEntry.get(1.0,"end-1c")
        mark = MarkEntry.get(1.0,"end-1c")
        db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
        mycursor=db.cursor()
        try:
           mycursor.execute("INSERT INTO `coursework`.`titles`(`genre_id`, `name`, `description`, `author_id`,`mark`) VALUES('"+str(id)+"', '"+str(name)+"', '"+str(desc)+"','1', '"+str(mark)+"')")

           db.commit()
           messagebox.showinfo("Справка","запись добавлена")
           search()
           clear()
        except EXCEPTION as e:
           print(e)
           db.rollback()
           db.close()

def update():
    id = idEntry.get()
    name = nameEntry.get(1.0, "end-1c")
    desc = descEntry.get(1.0, "end-1c")
    mark = MarkEntry.get(1.0, "end-1c")
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    mycursor.execute("UPDATE `coursework`.`titles` SET `genre_id` = '"+str(id)+"', `name` = '"+str(name)+"', `description` = '"+str(desc)+"', `author_id` = '2', `mark` = '"+str(mark)+"' WHERE name = '"+str(name)+"'")

    db.commit()
    messagebox.showinfo("Справка", "Запись изменена")
    idEntry.delete(0, END)
    descEntry.delete("1.0", "end")
    MarkEntry.delete("1.0", "end")
    nameEntry.delete("1.0","end")
    search()
    clear()

def delete1():
    name = nameEntry.get(1.0, "end-1c")
    db = mysql.connector.connect(host="localhost", user="root", password="Am I so weird?", database="coursework")
    mycursor = db.cursor()
    sql = "DELETE FROM `coursework`.`titles` WHERE name='"+str(name)+"'"
    mycursor.execute(sql)
    db.commit()
    messagebox.showinfo("Справка", "Запись удалена успешно")
    idEntry.delete(0, END)
    descEntry.delete("1.0", "end")
    descentry.delete("1.0", "end")
    search()
    clear()



def clear():
    updatebt.configure(state = "disabled")
    deletebt.configure(state = "disabled")
    idEntry.configure(state='normal')
    idEntry.delete(0, END)
    MarkEntry.configure(state='normal')
    MarkEntry.delete("1.0", "end")
    descEntry.delete("1.0", "end")
    descentry.delete("1.0", "end")
    addbt.configure(state='normal')

header=Frame(root, bg="#23C3B8", bd=0)
header.place(x=0,y=0,width=900,height=75)


nsec = Label(header, text="База данных медиа файлов", font=("Helvetica", 18, "bold"), bg="orange", fg="#eae2b7")
nsec.place(x=0, y=10, width=900)

frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Тайтлы", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text = "Закрыть", command = on_closing, bd = 0, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=820, y=0, height = 50, width = 80)
# LEFT BOX
leftbox=Frame(root,bd=0,bg="brown")
leftbox.place(x=10,y=140,width=500,height=350)


leftbox_title=Label(leftbox,text="Управление БД",font=("Helvetica",20,"bold"),fg="#eae2b7",bg="brown")
leftbox_title.place(x=10, y=30, width=  500)
iDLabel=Label(leftbox, text="id жанра", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
iDLabel.place(x=10, y =90)
idEntry=Entry(leftbox, font=("Helvetica", 15), bd=0)
idEntry.place(x=160, y =90, width = 317)
namelabel=Label(leftbox, text="Название", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
namelabel.place(x=10, y=120)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
nameEntry=Text(leftbox, font=("Helvetica", 15), bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=nameEntry.yview)
nameEntry.place(x=160, y=120, width = 300, height = 70)
scrolly.place(x=460, y=120, height = 70)
descLabel=Label(leftbox, text="Описание", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
descLabel.place(x=10, y=190)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
descEntry=Text(leftbox, font=("Helvetica", 15), bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=descEntry.yview)
descEntry.place(x=160, y=195, width = 300, height = 70)
scrolly.place(x=460, y=195, height = 30)
MarkLabel=Label(leftbox,text="Оценка",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
MarkLabel.place(x=10, y=245)
MarkEntry=Text(leftbox, font=("Helvetica", 15),bd=0, yscrollcommand=scrolly.set)
MarkEntry.place(x=160, y=260, width = 300, height = 20)



btnfrm=Frame(leftbox, bd=0, bg="brown")
btnfrm.place(x=0,y=300,width=500,height=50)

addbt=Button(btnfrm,text="Добавит",font=("Helvetica", 12),bg="indianred",fg="white",bd=0,command=add)
addbt.place(x=50, y=0, width = 70)
updatebt=Button(btnfrm,text="Изменить",font=("Helvetica", 12),bg="indianred",fg="white",bd=0,command=update)
updatebt.configure(state = "disabled")
updatebt.place(x=150, y=0, width = 70)
deletebt=Button(btnfrm,text="Удалить",font=("Helvetica", 12),bg="indianred",fg="white",command=delete1, bd =0)
deletebt.configure(state = "disabled")
deletebt.place(x=250, y=0, width = 70)
clrbt=Button(btnfrm,text="Очистить",font=("Helvetica", 12),bg="indianred",fg="white",command=clear, bd = 0)
clrbt.place(x=350, y=0, width = 70)


rightbox=Frame(root,bd=0,bg="indianred")
rightbox.place(x=500,y=140,width=390,height=350)


searchInput=Entry(rightbox,font=("Helvetica", 12),bd=0,width=17)
searchInput.place(x=10, y=10, height = 30)
dropdown=ttk.Combobox(rightbox,font=("Helvetica",10),state='readonly', width = 10)
dropdown['values']=("--поиск по--", "Name", "Genre_id")
dropdown.current(0)
dropdown.place(x=180, y=10, height = 30)
searchBtn=Button(rightbox,text="Поиск",command=search,font=("Helvetica", 12),width=10, bd = 0)
searchBtn.place(x=280, y=10, height = 30)


tabfrm=Frame(rightbox,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=50,width=370,height=270)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
data_table=ttk.Treeview(tabfrm,columns=("title_id","genre_id", "name","description","mark"),yscrollcommand=scrolly.set)
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=data_table.yview)

note_text=Label(rightbox,font=("Helvetica", 10),bg="indianred",fg="white")
note_text.place(x=10, y=325)


data_table.heading("title_id",text="title_id")
data_table.heading("genre_id",text="genre_id")
data_table.heading("name",text="name")
data_table.heading("description",text="description")
data_table.heading("mark",text="mark")
data_table['show']="headings"
data_table.column("title_id",width = 10)
data_table.column("genre_id",width=50)
data_table.column("name",width=30)
data_table.column("description",width=50)
data_table.column("mark",width=30)
data_table.pack(fill=BOTH,expand=1)
data_table.bind("<ButtonRelease-1>",getdata)
search()



root.mainloop()