from tkinter import *
from tkinter import ttk
import re

# root window
root = Tk()
root.geometry("400x200")
root.title("Temperature converter")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.minsize(400, 200)
root.maxsize(400, 200)
frame = ttk.Frame(root)
frame.grid()
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
# x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
# y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (800, 500))


def is_valid(newval):
    result = re.match("\d{0,5}$", newval) is not None
    if not result and len(newval) <= 3:
        errmsg.set(" Доступен ввод только цифр! ")
    else:
        errmsg.set("")
    return result


def get_value(*args):
    x = int(celsius_enter.get())
    y = str(x * 9 / 5 + 32)
    resultsContents.set(y)


# Error label
check = (root.register(is_valid), "%P")
errmsg = StringVar()
error_label = ttk.Label(frame, foreground="red", textvariable=errmsg)
error_label.grid(row=3, column=0, columnspan=2, sticky=N)

# Celsius Label+Enter
celsius_label = ttk.Label(frame, text="Celsius: ")
celsius_label.grid(row=0, column=0)
celsius_enter = ttk.Entry(frame, validate="key", validatecommand=check)
celsius_enter.focus()
celsius_enter.grid(row=0, column=1, sticky="W")

# Fahrenheit Label+ Value
fahrenheit_label = ttk.Label(frame, text="Fahrenheit: ")
fahrenheit_label.grid(row=1, column=0)

resultsContents = StringVar()

fahrenheit_meaning = ttk.Label(frame)
fahrenheit_meaning['textvariable'] = resultsContents
fahrenheit_meaning.grid(row=1, column=1)

resultsContents.set("Insert value")

# Button
convert_button = ttk.Button(frame, text="Cenvert", command=get_value)
convert_button.grid(row=2, column=0, columnspan=2)

root.bind("<Return>", get_value)
root.mainloop()
