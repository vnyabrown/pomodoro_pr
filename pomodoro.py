import datetime
import sqlite3
from flask import Flask, render_template, url_for, current_app, g, request, flash, redirect

pomodoro = Flask(__name__)
pomodoro.config['SECRET_KEY'] = 'C977F4FDFDD46C483B9B1596ED213'

# Set up database and temporary data
connection = sqlite3.connect('pomos.db')

with open('testdb.sql') as f:
    connection.executescript(f.read()) # run our initial sql file

cur = connection.cursor() # create a cursor to use w/ db connection

# put initial data for testing
cur.execute("INSERT INTO tasks (title, content, task_time) VALUES (?, ?, ?)",
            ('Test Task 1', 'This is a test!', '30')
            )
cur.execute("INSERT INTO tasks (title, content, task_time) VALUES (?, ?, ?)",
            ("Test Task 2", 'This is another test!', '30')
            )
connection.commit()
connection.close()

def get_db_conn():
    conn = sqlite3.connect('pomos.db')
    conn.row_factory = sqlite3.Row
    return conn

# running

@pomodoro.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        task_time = request.form['task_time']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        elif not task_time:
            flash('Task time is required!')
        else:
            conn = get_db_conn()
            conn.execute('INSERT INTO tasks (title, content, task_time) VALUES (?, ?, ?)',
                         (title, content, task_time))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    else:
        conn = get_db_conn()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        conn.close()
        return render_template('index.html', tasks=tasks)
    

if __name__ == "__main__":
    pomodoro.run(debug=True)