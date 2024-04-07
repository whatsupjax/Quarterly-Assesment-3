import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import subprocess

def start_quiz():
    selected_table = tableCombobox.get()
    if selected_table:
        subprocess.Popen(['python', 'QuizWindow.py', selected_table])
        root.destroy()

con = sql.connect('QuizKey.db')  # Corrected database name
cur = con.cursor()
table_names = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
table_names = [name[0] for name in table_names]

root = tk.Tk()
root.title('Quiz Selector')

tableLabel = tk.Label(root, text='Select a quiz table:')
tableLabel.pack()

tableCombobox = ttk.Combobox(root, values=table_names)
tableCombobox.pack()

startQuizButton = tk.Button(root, text='Start Quiz', command=start_quiz)
startQuizButton.pack()

root.mainloop()
