from flask import Flask,  render_template, url_for
from flask_socketio import SocketIO,emit,send
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
socket = SocketIO(app)

@socket.on('start_all')
def start_all():
        emit('start_all',"this text is from the server")
     

@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    socket.run(app,host="192.168.1.4",debug=True) #change host to your local ip
   

