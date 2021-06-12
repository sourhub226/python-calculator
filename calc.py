from tkinter import Button, Entry, Frame, StringVar, Tk
from tkinter.constants import BOTH, LEFT, RIGHT, TOP, X, Y
from asteval import Interpreter
aeval = Interpreter()

calc = Tk()
calc.title("Calculator")
calc_width = 400
calc_height = 620
calc.geometry("%dx%d" % (calc_width, calc_height))
calc.minsize(calc_width, calc_height)
calc.configure(background="#191919")

container = Frame(calc, bg="#202125")
container.pack(fill=Y, expand=True)


class Global:
    def __init__(self):
        self.flag = 0
        self.scval = StringVar()


Global = Global()


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if Global.scval.get().isdigit():
            value = int(Global.scval.get())
        else:
            try:
                value = round(aeval(screen.get()), 6)
            except ZeroDivisionError:
                show_error("Math Error")
            except Exception:
                show_error("Invalid Exp")
        Global.scval.set(value)
        screen.config(fg="white")
        Global.flag = 1

    elif text == "C":
        Global.scval.set("")
        screen.config(fg="white")
    else:
        if Global.flag:
            Global.scval.set("")
            screen.config(fg="white")
        Global.scval.set(Global.scval.get() + text)
        Global.flag = 0


def show_error(errormsg):
    screen.config(fg="red")
    Global.scval.set(errormsg)
    Global.flag = 1


screen = Entry(
    container,
    textvar=Global.scval,
    font="arial 40",
    bg="#303135",
    bd=0,
    fg="white",
    justify=RIGHT,
    insertbackground="#0851df",
)
screen.pack(fill=BOTH, expand=True, side=TOP)

left_f = Frame(container, bg="#202125")
left_f.pack(side=LEFT, fill=X, expand=True)
right_f = Frame(container, bg="#0851df")
right_f.pack(side=LEFT, fill=BOTH, expand=True)

btn_list = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", ".", "="]
for btn in btn_list:
    index = btn_list.index(btn)
    if index % 3 == 0:
        f = Frame(left_f, bg="#202125")
        f.pack(fill=BOTH, expand=True)

    b = Button(
        f,
        text=btn,
        font="consolas 28 bold",
        padx=20,
        pady=25,
        bd=0,
        fg="white",
        bg="#202125",
        activebackground="#404145",
        activeforeground="white",
    )
    b.pack(fill=BOTH, expand=True, side=LEFT)
    b.bind("<Button>", click)

btn_list = ["C", "/", "*", "-", "+"]
for btn in btn_list:
    b = Button(
        right_f,
        text=btn,
        font="lucida 25 bold",
        pady=20,
        bd=0,
        fg="white",
        bg="#0851df",
        activebackground="#2871ff",
        activeforeground="white",
    )
    b.pack(fill=BOTH, expand=True)
    b.bind("<Button>", click)

calc.mainloop()
