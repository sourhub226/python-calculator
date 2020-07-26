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

    elif text=='C':
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
calc_width=400
calc_height=620
calc.geometry("%dx%d"%(calc_width,calc_height))
calc.minsize(calc_width,calc_height)
calc.configure(background="#191919")

container=Frame(calc,bg="#202125")
container.pack(fill=Y,expand=True)

flag=0
scval=StringVar()
screen=Entry(container,textvar=scval,font="arial 40",bg="#303135",bd=0,fg ='white',justify=RIGHT,insertbackground='#0851df')
screen.pack(fill=BOTH,expand=True,side=TOP)

left_f=Frame(container,bg="#202125")
left_f.pack(side=LEFT,fill=X,expand=True)
right_f=Frame(container,bg="#0851df")
right_f.pack(side=LEFT,fill=BOTH,expand=True)

btn_list=["7","8","9","4","5","6","1","2","3","0",".","="]
for btn in btn_list:
    index=btn_list.index(btn)
    if (index%3==0):
        f=Frame(left_f,bg="#202125")
        f.pack(fill=BOTH,expand=True)
    
    b= Button(f, text=btn,font="consolas 28 bold",padx=20,pady=25,bd=0,fg ='white',bg="#202125",activebackground='#404145',activeforeground="white")
    b.pack(fill=BOTH,expand=True,side=LEFT)
    b.bind("<Button>",click)

btn_list=["C","/","*","-","+"]
for btn in btn_list:
    b= Button(right_f, text=btn,font="lucida 25 bold",pady=20,bd=0,fg ='white',bg="#0851df",activebackground='#2871ff',activeforeground="white")
    b.pack(fill=BOTH,expand=True)
    b.bind("<Button>",click)

calc.mainloop()