# Как работает программа?
Так, при написании плана, он с помощью моей БД  уходит в файл `JSON`, и выводится на `label` с помощью цикла `for` и `def update_labels()`

# Сейчас ChatGPT обьяснит код, ведь мне лень
- Импорт библиотек:

```python
from os import system
from datetime import datetime
```
В этой части кода происходит импорт необходимых модулей. Модуль system из библиотеки os используется для выполнения команд в командной строке. Модуль `datetime` используется для работы с датами и временем.

- Обработка исключений и импорт библиотек:

```python
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
```
В этой части кода используется блок `try-except`, чтобы проверить наличие необходимых библиотек (`barladb` и `tkinter`). Если библиотеки не найдены, программа попытается установить их с помощью команды `system("pip install ...")` и затем импортировать их. Если установка не удалась, возможно, будет сгенерировано исключение, которое будет поймано блоком except.

- Основные функции планера:

```python
def remove_plan(plan):
    # ... ваш код ...

def update_labels():
    # ... ваш код ...

def add(event=None):
    # ... ваш код ...
```
Здесь определены три основные функции:

`remove_plan(plan)`: Удаляет задачу из списка планов по заданному тексту задачи `plan`.
`update_labels()`: Обновляет отображение списка планов и соответствующих им чекбоксов на основе данных, хранящихся в переменной `data`.
`add(event=None)`: Добавляет новую задачу в список планов и вызывает `update_labels()` для обновления интерфейса.

- Создание графического интерфейса с помощью Tkinter:

```python
root = Tk()
root.geometry("500x500")
root.iconbitmap("Calendar.ico")
root.title("Планер задач")
root.resizable(False, False)
```
Здесь создается главное окно (`root`) для графического интерфейса с размерами 500x500 пикселей, заголовком "Планер задач" и иконкой, указанной в файле `"Calendar.ico"`. Вызов `root.resizable(False, False)` делает окно неизменным по размеру, то есть пользователь не может изменить его размер.

- Создание виджетов и размещение их на окне:

```python
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
```
Здесь создаются различные виджеты для ввода планов, отображения сообщений и списка задач. Ввод планов осуществляется через `Entry` с именем `entry_New`, кнопка "Добавить" связана с функцией `add()`. Результаты добавления и ошибки выводятся с помощью `Label` с именем `planinplan_label`.

Вызов функции `update_labels()`, чтобы отобразить список задач при запуске:

```python
labels = []
checkbuttons = []
update_labels()

root.mainloop()
```
Здесь создаются списки `labels` и `checkbuttons` для хранения созданных `Label` и `Checkbutton`. Затем вызывается функция `update_labels()` для отображения списка задач при запуске приложения. После этого происходит запуск главного цикла событий методом `root.mainloop()`, который позволяет окну взаимодействовать с пользователем.