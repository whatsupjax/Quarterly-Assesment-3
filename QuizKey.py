import sqlite3

con = sqlite3.connect('QuizKey.db')
cur = con.cursor()

DS3850QABank = [('1', 'Question 1', 'Answer 1'),
                ('2', 'Question 2', 'Answer 2'),
                ('3', 'Question 3', 'Answer 3'),
                ('4', 'Question 4', 'Answer 4'),
                ('5', 'Question 5', 'Answer 5')]

ECON3320QABank = [('1', 'Question 1', 'Answer 1'),
                  ('2', 'Question 2', 'Answer 2'),
                  ('3', 'Question 3', 'Answer 3'),
                  ('4', 'Question 4', 'Answer 4'),
                  ('5', 'Question 5', 'Answer 5')]

DS3841QABank = [('1', 'Question 1', 'Answer 1'),
                ('2', 'Question 2', 'Answer 2'),
                ('3', 'Question 3', 'Answer 3'),
                ('4', 'Question 4', 'Answer 4'),
                ('5', 'Question 5', 'Answer 5')]

DS3865QABank = [('1', 'Question 1', 'Answer 1'),
                ('2', 'Question 2', 'Answer 2'),
                ('3', 'Question 3', 'Answer 3'),
                ('4', 'Question 4', 'Answer 4'),
                ('5', 'Question 5', 'Answer 5')]

FIN3210QABank = [('1', 'Question 1', 'Answer 1'),
                 ('2', 'Question 2', 'Answer 2'),
                 ('3', 'Question 3', 'Answer 3'),
                 ('4', 'Question 4', 'Answer 4'),
                 ('5', 'Question 5', 'Answer 5')]

DS3850Table = cur.execute('''CREATE TABLE IF NOT EXISTS DS3850
                     (ids INTEGER PRIMARY KEY,
                     question VARCHAR,
                     answer VARCHAR)''')

ECON3320Table = cur.execute('''CREATE TABLE IF NOT EXISTS ECON3320
                     (ids INTEGER PRIMARY KEY,
                     question VARCHAR,
                     answer VARCHAR)''')

DS3841Table = cur.execute('''CREATE TABLE IF NOT EXISTS DS3841
                     (ids INTEGER PRIMARY KEY,
                     question VARCHAR,
                     answer VARCHAR)''')

DS3865Table = cur.execute('''CREATE TABLE IF NOT EXISTS DS3865
                     (ids INTEGER PRIMARY KEY,
                     question VARCHAR,
                     answer VARCHAR)''')

FIN3210Table = cur.execute('''CREATE TABLE IF NOT EXISTS FIN3210
                     (ids INTEGER PRIMARY KEY,
                     question VARCHAR,
                     answer VARCHAR)''')

for value in DS3850QABank:
    cur.execute('''INSERT INTO DS3850 (ids, question, answer)
                           VALUES (?, ?, ?)''', value)

for value in ECON3320QABank:
    cur.execute('''INSERT INTO ECON3320 (ids, question, answer)
                           VALUES (?, ?, ?)''', value)
    
for value in DS3841QABank:
    cur.execute('''INSERT INTO DS3841 (ids, question, answer)
                           VALUES (?, ?, ?)''', value)
    
for value in DS3865QABank:
    cur.execute('''INSERT INTO DS3865 (ids, question, answer)
                           VALUES (?, ?, ?)''', value)
    
for value in FIN3210QABank:
    cur.execute('''INSERT INTO FIN3210 (ids, question, answer)
                           VALUES (?, ?, ?)''', value)
    
con.commit()