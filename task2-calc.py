from tkinter import *
root=Tk()
root.title("Simple calculator")
root.geometry("414x530+500+100")
root.configure(bg="black")

lbl=Label(root, height=2, width=25, font="verdana 20", text="")
lbl.pack()

answer=""
def clear():
    global answer
    answer=""
    lbl.config(text=answer)

def equals():
    global answer
    result=""
    try:
        result=str(eval(answer))
        answer=""
        lbl.config(text=result)
    except:
        clear()
        lbl.config(text="Error")
    

def calc(symbol):
    global answer
    answer+=str(symbol)
    lbl.config(text=answer)
    

btnclr=Button(root, text="C", font=("verdana", 20), bg="black", fg="white", height=1, width=5, command= lambda: clear()).place(x=4, y=75)
btnper=Button(root, text="%", font=("verdana", 20), bg="black", fg="white", height=1, width=5, command= lambda: calc("%")).place(x=107, y=75)
btndiv=Button(root, text="/", font=("verdana", 20), bg="black" , fg="white", height=1, width=5, command= lambda: calc("/")).place(x=210, y=75)
btnmul=Button(root, text="*", font=("verdana", 20), bg="black", fg="white", height=1, width=5, command= lambda: calc("*")).place(x=314, y=75)
btnsub=Button(root, text="-", font=("verdana", 20), bg="black", fg="white", height=3, width=5, command= lambda: calc("-")).place(x=314, y=140)
btnadd=Button(root, text="+", font=("verdana", 20), bg="black", fg="white", height=3, width=5, command= lambda: calc("+")).place(x=314, y=270)
btneq=Button(root, text="=", font=("verdana", 20), bg="black", fg="white", height=3, width=5, command= lambda: equals()).place(x=314, y=400)

btn7=Button(root, text="7", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("7")).place(x=4, y=140)
btn8=Button(root, text="8", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("8")).place(x=107, y=140)
btn9=Button(root, text="9", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("9")).place(x=210, y=140)

btn4=Button(root, text="4", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("4")).place(x=4, y=238)
btn5=Button(root, text="5", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("5")).place(x=107, y=238)
btn6=Button(root, text="6", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("6")).place(x=210, y=238)

btn1=Button(root, text="1", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("1")).place(x=4, y=336)
btn2=Button(root, text="2", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("2")).place(x=107, y=336)
btn3=Button(root, text="3", font=("verdana", 20), bg="black", fg="white", height=2, width=5, command= lambda: calc("3")).place(x=210, y=336)

btn0=Button(root, text="0", font=("verdana", 20), bg="black", fg="white", height=2, width=8, command= lambda: calc("0")).place(x=4, y=434)
btndot=Button(root, text=".", font=("verdana", 20), bg="black", fg="white", height=2, width=8, command= lambda: calc(".")).place(x=160, y=434)

root.mainloop()



