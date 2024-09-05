import tkinter
from tkinter import *
# Create an app window
window = Tk()
# Add the app name
window.title('Поиск новых целей (уплотнение)')
# set window size
window.geometry('500x300')
# Add button for set files
readme = tkinter.Label(text = "Необходимо выбрать выгрузку из ПО РН-КИН, данные гис с информацией по всем интервалами перфорации")
readme.pack()
button = tkinter.Button(text = "Выберите файл с базой данных")
button.pack()
window.mainloop()