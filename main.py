from os import system
from datetime import datetime
try:
    from barladb import db
except:
    system("pip install barladb")
    from barladb import db
try:
    from tkinter import *
    from tkinter import ttk
except:
    system("pip install tkinter")
    from tkinter import *
    from tkinter import ttk

def remove_plan(plan):
    plans = data["plans"]
    plans.remove(plan)
    data["plans"] = plans
    db.save("data", data)
    update_labels()

def update_labels():
    for label, checkbutton in zip(labels, checkbuttons):
        label.grid_forget()
        checkbutton.grid_forget()

    for i, plan in enumerate(data["plans"]):
        label = ttk.Label(frame, text=plan)
        checkbutton = ttk.Checkbutton(frame, command=lambda plan=plan: remove_plan(plan))
        label.grid(column=0, row=i + 2, sticky=W)
        checkbutton.grid(column=1, row=i + 2, sticky=W)
        labels.append(label)
        checkbuttons.append(checkbutton)

def add(event=None):
    plan = entry_New.get()
    entry_New.delete(0, END)

    plans = data["plans"]
    
    if plan == "":
        planinplan.set("Ваш план не может быть пустым!")
    elif plan == "Ваш план":
        planinplan.set("Ошибка!")
    elif plan not in plans:
        planinplan.set("")
        plans.append(plan)
        data["plans"] = plans
        db.save("data", data)
        update_labels()
    else:
        planinplan.set(f"{plan} уже существует в Ваших планах.")

root = Tk()
root.geometry("500x500")
root.iconbitmap("Calendar.ico")
root.title("Планер задач")
root.resizable(False, False)

planinplan = StringVar()
data = db.get("data")

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

entry_Label = ttk.Label(frame, text="План: ")
entry_Label.grid(column=0, row=0, sticky=W)
entry_New = ttk.Entry(frame)
entry_New.insert(0, "Ваш план")
entry_New.bind("<Return>", add)
entry_New.grid(column=0, row=1, sticky=W)
entry_Button = ttk.Button(frame, text="Добавить", command=add)
entry_Button.grid(column=1, row=1, sticky=W)

planinplan_label = ttk.Label(textvariable=planinplan, wraplength=250)
planinplan_label.grid(column=0, row=1, sticky=W)

labels = []
checkbuttons = []
update_labels()

root.mainloop()