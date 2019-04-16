from tkinter import *


root = Tk()

formula = ""

equation = StringVar()
equation.set("0")

calculation = Label(root, textvariable = equation)
calculation.grid(row=0, columnspan = 4)

def pressBtn(num):
    global formula #informs the function that there is a global formula outside of the function to be used!
    formula = formula + str(num)
    equation.set(formula)

def equalBtn(): # dont have to pass anything
    global formula
    result = str(eval(formula)) #eval turns strings into python code , it will automatically executes!, then convert the results in to string!
    equation.set(result)
    formula = ""

def clearBtn():
    global formula
    formula = ""
    equation.set(formula)



btn_1 = Button(root, text="1", padx=15, pady=15, command= lambda: pressBtn(1)) #lambda enables as no name function, its not executing anything until we click
btn_1.grid(row=1, column=0)

btn_2 = Button(root, text="2", padx=15, pady=15, command= lambda: pressBtn(2))
btn_2.grid(row=1, column=1)

btn_3 = Button(root, text="3", padx=15, pady=15, command= lambda: pressBtn(3))
btn_3.grid(row=1, column=2)

btn_plus = Button(root, text="+", padx=15, pady=15, command= lambda: pressBtn("+"))
btn_plus.grid(row=1, column=3)

btn_4 = Button(root, text="4", padx=15, pady=15, command= lambda: pressBtn(4))
btn_4.grid(row=2, column=0)

btn_5 = Button(root, text="5", padx=15, pady=15, command= lambda: pressBtn(5))
btn_5.grid(row=2, column=1)

btn_6 = Button(root, text="6", padx=15, pady=15, command= lambda: pressBtn(6))
btn_6.grid(row=2, column=2)

btn_minus = Button(root, text="-", padx=15, pady=15, command= lambda: pressBtn("-"))
btn_minus.grid(row=2, column=3)

btn_7 = Button(root, text="7", padx=15, pady=15, command= lambda: pressBtn(7))
btn_7.grid(row=3, column=0)

btn_8 = Button(root, text="8", padx=15, pady=15, command= lambda: pressBtn(8))
btn_8.grid(row=3, column=1)

btn_9 = Button(root, text="9", padx=15, pady=15, command= lambda: pressBtn(9))
btn_9.grid(row=3, column=2)

btn_times = Button(root, text="*", padx=15, pady=15, command= lambda: pressBtn("*"))
btn_times.grid(row=3, column=3)

btn_0 = Button(root, text="0", padx=15, pady=15, command= lambda: pressBtn(0))
btn_0.grid(row=4, column=0)

btn_clear = Button(root, text="C", padx=15, pady=15, command= clearBtn)
btn_clear.grid(row=4, column=1)

btn_equal = Button(root, text="=", padx=15, pady=15, command= equalBtn)
btn_equal.grid(row=4, column=2)

btn_divide = Button(root, text="/", padx=15, pady=15, command= lambda: pressBtn("/"))
btn_divide.grid(row=4, column=3)

root.mainloop()
