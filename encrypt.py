#Modified Caesar Cipher
from tkinter import *
def main():
    txt.delete(0.0,'end')
    str = ent1.get()
    key = ent2.get()
    crypto = var_chk.get()
    if crypto == 1:
        encrypted = ''
        i = len(key)
        f = 0
        for x in str:
            if f == i:
                f = 0
            indx = (ord(x) + int(key[f])) % 256
            if indx > 126:
                indx = indx - 95
            encrypted = encrypted + chr(indx)
            f = f + 1
        txt.insert(0.0,encrypted)
    else:
        decrypted = ''
        i = len(key)
        f = 0
        for x in str:
            if f == i:
                f = 0
            indx = (ord(x) - int(key[f])) % 256
            if indx < 32:
                indx = indx + 95
            decrypted = decrypted + chr(indx)
            f = f + 1
        txt.insert(0.0,decrypted)

root = Tk()
root.geometry("300x300")
root.configure(background="blue")

#Creating Widgts
message = Label(root ,font="lucida 8 bold",bg="blue",fg="white",text = "Message:")
keyBtn = Label(root ,font="lucida 8 bold",bg="blue" ,fg="white",text = "key:")

ent1 = Entry(root, font="lucida 12 bold",fg="blue",width = 37)
ent2 = Entry(root,font="lucida 12 bold", fg="blue",width = 37)

var_chk = IntVar()

rb1 = Radiobutton(root , font="lucida 8 bold",text = "encrypt" ,variable = var_chk , value = 1)
rb2 = Radiobutton(root ,font="lucida 8 bold", text = "decrypt" ,variable = var_chk , value = 2)

bt = Button(root , text = "Submit" , font="lucida 12 bold",bg = "blue" , fg= "white" ,  command = main)

bt2 = Button(root , text = "Exit" , font="lucida 12 bold",bg = "blue" , fg= "white" ,  command = exit)


txt = Text(root ,fg="blue",font="lucida 12 bold", width = 37 , height = 12 , wrap = WORD)


#Placing them on screen
message.pack(padx=20,pady=20)
ent1.pack(padx=20,pady=20)

keyBtn.pack(padx=20,pady=20)
ent2.pack(padx=20,pady=20)

rb1.pack(padx=20,pady=20)
rb2.pack(padx=20,pady=20)
bt.pack(padx=20,pady=20)
txt.pack(padx=20,pady=20)
bt2.pack(padx=20,pady=20)
root.mainloop()