import tkinter as tk
from helpers.Project import Project

project = Project()

def undo_action():
    project.undo()

def redo_action():
    project.redo()

root = tk.Tk()

undo_button = tk.Button(root, text="Undo", command=undo_action)
redo_button = tk.Button(root, text="Redo", command=redo_action)

undo_button.pack()
redo_button.pack()

root.mainloop()