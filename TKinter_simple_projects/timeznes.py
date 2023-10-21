from tkinter import *
from tkinter import ttk
import datetime
import pytz

# Root window
root = Tk()
root.title("Timezone Check")
root.geometry("800x600")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.resizable(False, False)
root.wm_geometry("+%d+%d" % (700, 300))
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# examples StringVar
examples = StringVar()
examples.set("""
    {0:15} {1:15} {2:15}
    {3:23} {4:16} {5:15}
    {6:23} {7:19} {8:15}
    {9:23} {10:14} {11:15}
    {12:25} {13:17} {14:15}
    {15:25} {16:18} {17:15}
    """.format("Код страны", "Страна", "Часовой пояс",
               "HR", "Croatia", "Europe/Zagreb",
               "HT", "Haiti", "America/Port-au-Prince",
               "HU", "Hungary", "Europe/Budapest",
               "IE", "Ireland", "Europe/Dublin",
               "IL", "Israel", "Asia/Jerusalem"
               ))

results_str_var = StringVar()
errmsg = StringVar()


def cod_country(*args):
    x = enter_country_entry.get().upper()
    if x == "Q":
        root.destroy()
    try:
        name_of_country = pytz.country_names[f"{x}"]
        name_time_zone = pytz.country_timezones.get(f"{x}")
        tz = pytz.timezone(str(name_time_zone[0]))
        date_time = datetime.datetime.now(tz=tz)
        results_str_var.set(f"В {name_of_country} сейчас {date_time.strftime('%d/%m/%Y, %H:%M:%S')} ")
        errmsg.set("")
    except KeyError:
        errmsg.set("Введите корректный код страны")
        results_str_var.set("")


stat_label = ttk.Label(frame, text="Узнаем время в другой стране?")
example_country = ttk.Label(frame, textvariable=examples)
quit_label = ttk.Label(frame, text="Для выхода введите 'Q'")
enter_country_label = ttk.Label(frame, text="Пожалуйста, введите двухзначный код страны: ", padding=20)
enter_country_entry = ttk.Entry(frame, width=10)
go_button = ttk.Button(frame, text="Go!", command=cod_country)
error_label = ttk.Label(frame, foreground="red", textvariable=errmsg, padding=20)
results_label = ttk.Label(frame, foreground="green", textvariable=results_str_var)

stat_label.grid(row=0, column=0, columnspan=2)
example_country.grid(row=1, column=0, columnspan=2)
quit_label.grid(row=2, column=0, columnspan=2)
enter_country_label.grid(row=3, column=0)
enter_country_entry.grid(row=3, column=1)
go_button.grid(row=6, column=0, columnspan=2)
results_label.grid(row=4, column=0, columnspan=2)
error_label.grid(row=5, column=0, columnspan=2, sticky=N)

root.bind("<Return>", cod_country)

root.mainloop()
