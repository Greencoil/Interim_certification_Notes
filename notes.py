from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

root = Tk()
root.title("Notes")
root.geometry("400x400")

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)

root.mainloop()