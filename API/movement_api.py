from flask import Flask
from settings import movement_port

app = Flask(__name__)

@app.route('/up')
def up():
    print('up')
    return ""


@app.route('/down')
def down():
    print('down')
    return ""

@app.route('/left')
def left():
    print('left')
    return ""

@app.route('/right')
def right():
    print('right')
    return ""

if __name__ == '__main__':
    app.run(port=movement_port)
