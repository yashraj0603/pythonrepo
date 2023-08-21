from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text=type,src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0,END)
    textget = change(text = masg,src = s,dest = d)    
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("language translater")
root.geometry("500x700")
root.config(bg='yellow')
lab_txt=Label(root,text="language translater",font=("Time New Romen",20,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)
frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="source text",font=("Time New Romen",10,"bold"),fg="blue",bg="yellow")
lab_txt.place(x=100,y=100,height=20,width=300)


sor_txt = Text(frame,font=("Time New Romen",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=200,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x=10,y=350,height=30,width=100)
comb_sor.set(("english"))

button_change=Button(frame,text="tranlate",relief=RAISED,command=data)
button_change.place(x=120,y=350,height=30,width=100)


comb_dest = ttk.Combobox(frame,values=list_text)
comb_dest.place(x=230,y=350,height=30,width=100)
comb_dest.set(("english"))

lab_txt=Label(root,text="dest text",font=("Time New Romen",10,"bold"),fg="blue",bg="yellow")
lab_txt.place(x=100,y=400,height=20,width=300)


dest_txt = Text(frame,font=("Time New Romen",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=430,height=200,width=480)

root.mainloop()
