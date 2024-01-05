from tkinter import *
root=Tk()
root.title("To Do List")
root.geometry("400x650+400+100")


def addItem():
    list=txt.get()
    lstbox.insert(END, list)
    values= lstbox.get(0,END)
    return


def done():
    indices=lstbox.curselection()
    newind= indices[::-1]
    for index in newind:
        lstbox.delete(index)
    return

heading=Label(root,text="\t\t\tTo Do List\t\t\t", font="helvetica 18 bold", fg="white", bg="black")
heading.pack(pady=20)

lbl=Label(root,text="Add item", font="verdana 14")
txt=Entry(root, font="verdana 14")

lbl.pack(padx=10, pady=10)
txt.pack(padx=10, pady=10)

btnAdd = Button(root, text="ADD", font="verdana 12", command=addItem)
btnAdd.pack(padx=10, pady=10)

lstbox = Listbox(root, height=10, width=15,  font="verdana 12", selectmode=MULTIPLE)
lstbox.pack(padx=10, pady=10)

btndone = Button(root, text="TASK DONE", font="verdana 12", command=done)
btndone.pack(padx=10, pady=10)

btnexit= Button(root, text="EXIT", font="verdana 12",command=root.destroy)
btnexit.pack(padx=10, pady=10)

lbl.pack()
root.mainloop()









