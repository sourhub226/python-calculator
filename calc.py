from tkinter import *
def click(event):
    global scval,flag
    #print("Click")
    text=event.widget.cget("text")
    #print(text)
    if text=='=':
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            try:
                value=eval(screen.get())
            except Exception:
                scval.set("Invalid Exp")
                screen.update()

        scval.set(value)
        screen.update()
        flag=1
        

    elif text=='Clear Input':
        scval.set("")
        screen.update()
    else:
        if flag==1:
            scval.set("")
            screen.update()
        scval.set(scval.get()+text)
        screen.update()
        flag=0

calc=Tk()
calc.title("Calculator")
calc.geometry("380x530")
calc.configure(background='#202125')

flag=0
scval=StringVar()
screen=Entry(calc,textvar=scval, font="arial 40",bg="#202125",bd=0,fg ='white',justify=RIGHT)
screen.pack(fill=X,ipady=5)

f=Frame(calc,bg="#202125")
f.pack()
b= Button(f, text="7",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="8",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="9",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="/",font="lucida 25 bold",pady=20,padx=34,bd=0,fg ='white',bg="#0851df")
b.pack(side=LEFT)
b.bind("<Button>",click)

f=Frame(calc,bg="#202125")
f.pack()
b= Button(f, text="4",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="5",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="6",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="*",font="lucida 25 bold",pady=20,padx=32,bd=0,fg ='white',bg="#0851df")
b.pack(side=LEFT)
b.bind("<Button>",click)

f=Frame(calc,bg="#202125")
f.pack()
b= Button(f, text="1",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="2",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="3",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="-",font="lucida 25 bold",pady=20,padx=33,bd=0,fg ='white',bg="#0851df")
b.pack(side=LEFT)
b.bind("<Button>",click)

f=Frame(calc,bg="#202125")
f.pack()
b= Button(f, text="0",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text=".",font="lucida 25 bold",pady=20,padx=34,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="=",font="lucida 25 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

b= Button(f, text="+",font="lucida 25 bold",pady=20,padx=29,bd=0,fg ='white',bg="#0851df")
b.pack(side=LEFT)
b.bind("<Button>",click)

f=Frame(calc,bg="#202125")
f.pack()
b= Button(f, text="Clear Input",font="lucida 18 bold",pady=20,padx=30,bd=0,fg ='white',bg="#202125")
b.pack(side=LEFT)
b.bind("<Button>",click)

calc.mainloop()