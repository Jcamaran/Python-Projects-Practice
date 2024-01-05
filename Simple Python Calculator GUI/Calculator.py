import tkinter as tk
from functools import partial

calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def eval_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
# From tkinter geometry() returns a table given a size in ""# 
root.geometry('300x400')
root.title('Simple Calculator')

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Using partial to pass arguments to add_to_calc function
btn_numbers = [
    tk.Button(root, text=str(i), command=partial(add_to_calc, i), width=5, font=("Arial", 14))
    for i in range(10)
]

#instead of writing out each button number, for loop to repeat the proccess faster #
for i in range(1, 10):
    btn_numbers[i].grid(row=(i - 1) // 3 + 2, column=(i - 1) % 3 + 1)
btn_numbers[0].grid(row=5, column=2)

operators = ['+', '-', '*', '/']

#enumerate is used to iterate over the list of operators above# 
for i, operator in enumerate(operators):
    tk.Button(root, text=operator, command=partial(add_to_calc, operator), width=5, font=("Arial", 14)).grid(row=i + 2, column=4)

tk.Button(root, text='(', command=partial(add_to_calc, '('), width=5, font=("Arial", 14)).grid(row=5, column=1)
tk.Button(root, text=')', command=partial(add_to_calc, ')'), width=5, font=("Arial", 14)).grid(row=5, column=3)

tk.Button(root, text='=', command=eval_calc, width=11, font=("Arial", 14)).grid(row=6, column=3, columnspan=2)
tk.Button(root, text='C', command=clear_field, width=5, font=("Arial", 14)).grid(row=6, column=1, columnspan=2)

root.mainloop()
