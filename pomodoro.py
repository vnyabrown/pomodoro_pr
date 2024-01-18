import datetime
import sqlite3
from flask import Flask, render_template, url_for, current_app, g, request

pomodoro = Flask(__name__)

# Set up database and temporary data
connection = sqlite3.connect('pomos.db')

with open('testdb.sql') as f:
    connection.executescript(f.read()) # run our initial sql file

cur = connection.cursor() # create a cursor to use w/ db connection

# put initial data for testing
cur.execute("INSERT INTO tasks (title, content) VALUES (?, ?)",
            ('Test Task 1', 'help')
            )
cur.execute("INSERT INTO tasks (title, content) VALUES (?, ?)",
            ("Test Task 2", 'help please')
            )
connection.commit()
connection.close()

def get_db_conn():
    conn = sqlite3.connect('pomos.db')
    conn.row_factory = sqlite3.Row
    return conn

# running

@pomodoro.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']

    else:
        conn = get_db_conn()
        task = conn.execute('SELECT * FROM tasks').fetchall()
        conn.close()
        return render_template('index.html')
    

if __name__ == "__main__":
    pomodoro.run(debug=True)