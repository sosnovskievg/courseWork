from tkinter import*
import mysql.connector
from tkinter import ttk
root =Tk()
root.title("Список постов")
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
        mycursor.execute("select user_table.user_id, post.post_id,titles.name, titles.description,authors.name from user_table inner join post on user_table.user_id = post.user_id inner join titles on post.title_id= titles.title_id inner join authors on titles.author_id= authors.author_id")
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

# IT WILL GET DATA IN LEFTBOX (getdata made events there and fecth value there also)
def getdata(event):
    currow = data_table.focus()
    contents = data_table.item(currow)
    row = contents['values']
    ThemeEntry.configure(state='normal')
    DescEntry.configure(state = 'normal')
    AuthortEntry.configure(state = 'normal')
    ThemeEntry.delete(0, END)
    DescEntry.delete("1.0", "end")
    AuthortEntry.delete("1.0", "end")
    ThemeEntry.insert(0, row[0])
    DescEntry.insert(END, row[3])
    AuthortEntry.insert(END, row[4])
    ThemeEntry.configure(state='readonly')
    DescEntry.configure(state = 'disabled')
    AuthortEntry.configure(state = 'disabled')

#Header
header=Frame(root, bg="#23C3B8", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec=Label(header, text="База данных медиа файлов",font=("Helvetica",36,"bold"), bg = "orange",fg="#eae2b7")
nsec.place(x=0, y=10, width=900)
#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Список постов", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text = "Close", command = on_closing, bd = 0, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)
# LEFT BOX
leftbox=Frame(root,bd=0,bg="#23C3B8")
leftbox.place(x=10,y=140,width=500,height=350)

# INSIDE LEFT BOX
leftbox_title=Label(leftbox,text="Автор поста",font=("Helvetica",20,"bold"),fg="#eae2b7",bg="brown")
leftbox_title.place(x=10, y=30, width=  500)
ThemeLabel=Label(leftbox,text="Тема",font=("Helvetica",15),fg="#eae2b7",bg="brown")
ThemeLabel.place(x=10, y =90)
ThemeEntry=Entry(leftbox,font=("Helvetica",15),bd=0)
ThemeEntry.place(x=160, y =90, width = 317)
DescLabel=Label(leftbox,text="Описание",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
DescLabel.place(x=10, y=140)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
DescEntry=Text(leftbox, font=("Helvetica", 15),bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=DescEntry.yview)
DescEntry.place(x=160, y=140, width = 300, height = 70)
scrolly.place(x=460, y=140, height = 70)
AuthorLabel=Label(leftbox,text="Автор",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
AuthorLabel.place(x=10, y=230)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
AuthortEntry=Text(leftbox, font=("Helvetica", 15),bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=AuthortEntry.yview)
AuthortEntry.place(x=160, y=235, width = 300, height = 70)
scrolly.place(x=460, y=235, height = 70)

# RIGHT BOX
rightbox=Frame(root,bd=0,bg="indianred")
rightbox.place(x=500,y=140,width=390,height=350)

# RIGHT BOX HEADING
searchInput=Entry(rightbox,font=("Helvetica", 12),bd=0,width=17)
searchInput.place(x=10, y=10, height = 30)
dropdown=ttk.Combobox(rightbox,font=("Helvetica",10),state='readonly', width = 10)
dropdown['values']=("--Search By--", "Тайтл", "Автору поста", "Автору произведения")
dropdown.current(0)
dropdown.place(x=180, y=10, height = 30)
searchBtn=Button(rightbox,text="Search",command=search,font=("Helvetica", 12),width=10, bd = 0)
searchBtn.place(x=280, y=10, height = 30)

# BOX INSIDE RIGHT BOX
tabfrm=Frame(rightbox,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=50,width=370,height=270)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
data_table=ttk.Treeview(tabfrm,columns=("Пользователь","Номер поста", "Название тайтла","Описание","Автор"),yscrollcommand=scrolly.set)
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=data_table.yview)

note_text=Label(rightbox,font=("Helvetica", 10),bg="indianred",fg="white")
note_text.place(x=10, y=325)

# INSIDE RIGHT BOX
data_table.heading("Пользователь",text="Пользователь")
data_table.heading("Номер поста",text="Номер поста")
data_table.heading("Название тайтла",text="Название")
data_table.heading("Описание",text="Описание")
data_table.heading("Автор",text="Автор")

data_table['show']="headings"
data_table.column("Пользователь",width = 5)
data_table.column("Номер поста",width=5)
data_table.column("Название тайтла",width=10)
data_table.column("Описание",width = 50)
data_table.column("Автор",width=10)
data_table.pack(fill=BOTH,expand=1)
data_table.bind("<ButtonRelease-1>",getdata)

search()

root.mainloop()