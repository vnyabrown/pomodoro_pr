import datetime
import sqlite3
from flask import Flask, render_template, url_for, current_app, g

pomodoro = Flask(__name__)

# Function to set up database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
        current_app.config['POMODORO_DATABASE'], 
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

    return g.db

# Function to close database
def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_recourse('testdb.sql') as f:
        db.executescript(f.read().decode('utf8'))

    def __repr__(self):
        return '<Task %r' % self.id

@pomodoro.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    pomodoro.run(debug=True)