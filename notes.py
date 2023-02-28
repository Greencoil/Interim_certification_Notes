from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file():
    global file_name
    file_name = "No name"
    text.delete('1.0', END)

root = Tk()
root.title("Notes")
root.geometry("600x600")

text = Text(root, width=600, height=600)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()