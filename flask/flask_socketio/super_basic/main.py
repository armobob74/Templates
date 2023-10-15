from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(msg):
    print('Received message:', msg)
    socketio.emit('message', 'Server received your message')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":  
    socketio.run(app)
