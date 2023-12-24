from tkinter import *
import random
root=Tk()
root.title("Password generator")
root.geometry("500x580+500+100")

l1=Label(root, text="Enter the length of password:", font="verdana 20")
e1=Entry(root, font="verdana 20")
l1.grid(row=0, column=0, padx=30, pady=10)
e1.grid(row=1, column=0, padx=10, pady=10)


statusr= IntVar()
radE=Radiobutton(root, text="Easy", font="verdana 15", value=1, var=statusr)
radM=Radiobutton(root, text="Medium", font="verdana 15", value=2, var= statusr)
radD=Radiobutton(root, text="Difficult", font="verdana 15", value=3, var=statusr)

radE.grid(row=2, column=0, padx=10, pady=10)
radM.grid(row=3, column=0, padx=10, pady=10)
radD.grid(row=4, column=0, padx=10, pady=10)

def display():
    uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters= "abcdefghjklmnopqrstuvwxyz"
    digits="0123456789"
    symbols= "()/<>&*%$^#@!;:"
    upper, lower, dig, sym= True, True, True, True
    all=""
    password=statusr.get()
    if password==1:
        if upper:
            all+=uppercase_letters
        if lower:
            all+=lowercase_letters
    elif password==2:
        if upper:
            all+=uppercase_letters
        if lower:
            all+=lowercase_letters
        if dig:
            all+=digits
    elif password==3:
        if upper:
            all+=uppercase_letters
        if lower:
            all+=lowercase_letters
        if dig:
            all+=digits
        if sym:
            all+=symbols
    amount = 10

    for _ in range(amount):
        password = "".join(random.sample(all, int(e1.get())))
    
    print(password)


btn=Button(root, text="Display", font="verdana 20", command=display)
btn.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()
