from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0,END)
        decodeMsg=message.encode("ascii")
        base64Bytes=base64.b64decode(decodeMsg)
        decrypt=base64Bytes.decode("ascii")
         
        Label(screen2,text="DECRYPTED MESSAGE",fg="black",font=("calbri",13),bg="#00bd56").place(x=30,y=10)
        text2=Text(screen2,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)
    elif password=="":
        messagebox.showerror("Encryption", "Enter a Secret Key")
    else:
        messagebox.showerror("Encryption", "Incorrect Secret Key")

def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encodeMsg=message.encode("ascii")
        base64Bytes=base64.b64encode(encodeMsg)
        encrypt=base64Bytes.decode("ascii")
        print(encrypt)
         
        Label(screen1,text="ENCRYPTED MESSAGE",fg="black",font=("calbri",13),bg="#ed3833").place(x=30,y=10)
        text2=Text(screen1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("Encryption", "Enter a Secret Key")
    else:
        messagebox.showerror("Encryption", "Incorrect Secret Key")
        
        
    


def main_screen():
    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("375x398")
    screen.title("TextCrypt")

    #icon
    icon=PhotoImage(file='./key.png')
    screen.iconphoto(False,icon)

    #resetButtonFunction
    def reset():
        code.set("")
        text1.delete(1.0,END)


    #Text
    Label(text="Enter Text for encryption or decryption",fg="black",font=("calbri",13)).place(x=30,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=150)
    #Secret KEY
    Label(text="Enter Secret Key",fg="black",font=("calbri",13)).place(x=10,y=210)
    code=StringVar()
    Entry(textvariable=code,width=10,bd=1,font=("arial",15),show='*').place(x=10,y=240,width=355,height=30)
    #Buttons
    Button(text="ENCRYPT",height="2",width="23",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=280)
    Button(text="DECRYPT",height="2",width="23",bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=280)
    Button(text="RESET",height="2",width="50",bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=325)


    screen.mainloop()
main_screen()