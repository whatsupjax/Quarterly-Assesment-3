import tkinter as tk
import sqlite3

class QuizApp:
    def __init__(self, master, table_name):
        self.master = master
        self.table_name = table_name
        self.quiz_data = []

        self.question_label = tk.Label(self.master, text='')
        self.question_label.pack()

        self.answer_label = tk.Label(self.master, text='Your Answer:')
        self.answer_label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.check_button = tk.Button(self.master, text='Check Answer', command=self.check_answer)
        self.check_button.pack()

        self.result_label = tk.Label(self.master, text='')
        self.result_label.pack()

        self.next_button = tk.Button(self.master, text='Next Question', command=self.show_question)
        self.next_button.pack()

        self.load_quiz_data()
        self.show_question()

    def load_quiz_data(self):
        con = sqlite3.connect('QuizKey.db')
        cur = con.cursor()
        self.quiz_data = cur.execute(f"SELECT question, answer FROM {self.table_name}").fetchall()
        con.close()

    def show_question(self):
        if self.quiz_data:
            question, answer = self.quiz_data.pop(0)  # Assuming the question is in index 0 and answer in index 1
            self.question_label.config(text=f'Question: {question}')
        else:
            self.question_label.config(text='Quiz completed!', fg='green')

    def check_answer(self):
        if self.quiz_data:
            user_answer = self.answer_entry.get()
            correct_answer = self.quiz_data[0][1]
            if user_answer.lower() == correct_answer.lower():
                self.result_label.config(text='Correct!', fg='green')
            else:
                self.result_label.config(text='Incorrect!', fg='red')
        else:
            self.result_label.config(text='No more questions!', fg='red')

root = tk.Tk()
root.title('Quiz Window')

# Provide a default table name if no table name is passed from the command line
table_name = 'default_table'

app = QuizApp(root, table_name)

root.mainloop()
