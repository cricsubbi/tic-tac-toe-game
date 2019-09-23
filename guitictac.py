#!C:\Users\subodh p\AppData\Local\Programs\Python\Python37-32\python.exe
from tkinter import *
from tkinter import messagebox

window = Tk()



window.title("THE X & O GAME")
window.geometry("600x300")
frame = Frame(window)
frame.grid()


lbl = Label(window, text="Welcome to tic-tac toe game",font=('Comic Sans MS', 20, 'bold'))
lbl.grid(row=0,column=0)
lbl = Label(window, text="PLAYER 1",font=('Comic Sans MS', 8))
lbl.grid(row=1,column=0)
lbl = Label(window, text="PLAYER 2",font=('Comic Sans MS', 8))
lbl.grid(row=2,column=0)


t=1

def c1():
    global t
    if t==1:
        t=2
        b1["text"]="X"
    elif t==2:
        t=1
        b1["text"]="O"
    check()

def c2():
    global t
    if t==1:
        t=2
        b2["text"]="X"
    elif t==2:
        t=1;
        b2["text"]="O"
    check()

def c3():
    global t
    if t==1:
        t=2
        b3["text"]="X"
    elif t==2:
        t=1;
        b3["text"]="O"
    check()

def c4():
    global t
    if t==1:
        t=2
        b4["text"]="X"
    elif t==2:
        t=1;
        b4["text"]="O"
    check()
        
def c5():
    global t
    if t==1:
        t=2
        b5["text"]="X"
    elif t==2:
        t=1;
        b5["text"]="O"
    check()

def c6():
    global t
    if t==1:
        t=2
        b6["text"]="X"
    elif t==2:
        t=1;
        b6["text"]="O"
    check()

def c7():
    global t
    
    if t==1:
        t=2
        b7["text"]="X"
    elif t==2:
        t=1;
        b7["text"]="O"
    check()


def c8():
    global t
    if t==1:
        t=2
        b8["text"]="X"
    elif t==2:
        t=1;
        b8["text"]="O"
    check()


def c9():
    global t
    
    if t==1:
        t=2
        b9["text"]="X"
    elif t==2:
        t=1;
        b9["text"]="O"
    check()


    
flag = 1

def check():
    
    global flag
    
    bb1 = b1["text"]
    bb2 = b2["text"]
    bb3 = b3["text"]
    bb4 = b4["text"]
    bb5 = b5["text"]
    bb6 = b6["text"]
    bb7 = b7["text"]
    bb8 = b8["text"]
    bb9 = b9["text"]

    flag = flag + 1
    
    if bb1==bb2 and bb1==bb3 and bb1=="O" or bb1==bb2 and bb1==bb3 and bb1=="X":
        win(b1["text"])
    if bb4==bb5 and bb4==bb6 and bb4=="O" or bb4==bb5 and bb4==bb6 and bb4=="X":
        win(b4["text"])
    if bb7==bb8 and bb7==bb9 and bb7=="O" or bb7==bb8 and bb7==bb9 and bb7=="X":
        win(b7["text"])
    if bb1==bb4 and bb1==bb7 and bb1=="O" or bb1==bb4 and bb1==bb7 and bb1=="X":
        win(b1["text"])
    if bb2==bb5 and bb2==bb8 and bb2=="O" or bb2==bb5 and bb2==bb8 and bb2=="X":
        win(b2["text"])
    if bb3==bb6 and bb3==bb9 and bb3=="O" or bb3==bb6 and bb3==bb9 and bb3=="X":
        win(b3["text"])
    if bb1==bb5 and bb1==bb9 and bb1=="O" or bb1==bb5 and bb1==bb9 and bb1=="X":
        win(b1["text"])
    if bb7==bb5 and bb7==bb3 and bb7=="O" or bb7==bb5 and bb7==bb3 and bb7=="X":
        win(b7["text"])
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!! Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins "
    messagebox.showinfo("Congratulations", ans)
    window.destroy()
    
b1 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c1)
b1.grid(row=3, column=2)

b2 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c2)
b2.grid(row=3, column=3)
b3 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c3)
b3.grid(row=3, column=4)

b4 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c4)
b4.grid(row=4, column=2)
b5 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic'),command=c5)
b5.grid(row=4, column=3)

b6 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c6)
b6.grid(row=4, column=4)
b7 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c7)
b7.grid(row=5, column=2)
b8 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c8)
b8.grid(row=5, column=3)
b9 = Button(window, text=" ",bg="blue", fg = "red",width=3,height=1,font=('times','20','italic','bold'),command=c9)
b9.grid(row=5, column=4)



            
window.mainloop()
