from tkinter import *

def click(event):
    global scval,flag
    text=event.widget.cget("text")
    if text=='=':
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            try:
                value=round(eval(screen.get()),6)
            except ZeroDivisionError:
                screen.config(fg="red")
                scval.set("Math Error")
                flag=1
            except Exception as e:
                screen.config(fg="red")
                scval.set("Invalid Exp")
                flag=1
        scval.set(value)
        screen.config(fg="white")
        flag=1

    elif text=='Clear Input':
        scval.set("")
        screen.config(fg="white")
    else:
        if flag:
            scval.set("")
            screen.config(fg="white")
        scval.set(scval.get()+text)
        flag=0

calc=Tk()
calc.title("Calculator")
calc_width=380
calc_height=520
calc.geometry("%dx%d"%(calc_width,calc_height))
calc.minsize(calc_width,calc_height)
calc.configure(background="#191919")

container=Frame(calc,width=13,bg="#202125")
container.pack(fill=Y,expand=True)

flag=0
scval=StringVar()
screen=Entry(container,textvar=scval,font="arial 40",bg="#303135",bd=0,fg ='white',justify=RIGHT,insertbackground='#0851df')
screen.pack(fill=Y,expand=True,ipady=5)

btn_list=["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]

for btn in btn_list:
    index=btn_list.index(btn)
    if (index%4==0):
        f=Frame(container,bg="#202125")
        f.pack(fill=BOTH,expand=True)
    
    if ((index+1)%4==0):
        b= Button(f, text=btn,font="consolas 25 bold",width=1,height=2,bd=0,fg ='white',bg="#0851df")
        b.pack(fill=BOTH,expand=True,side=LEFT)
        b.bind("<Button>",click)
    else:
        b= Button(f, text=btn,font="consolas 25 bold",width=1,height=2,bd=0,fg ='white',bg="#202125")
        b.pack(fill=BOTH,expand=True,side=LEFT)
        b.bind("<Button>",click)

b= Button(container, text="Clear Input",font="lucida 18 bold",bd=0,fg ='white',bg="#202125")
b.pack(ipady=10)
b.bind("<Button>",click)
calc.mainloop()