from flask import Flask
pomodoro = Flask(__name__)

@pomodoro.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    pomodoro.run(debug=True)
