from flask import Flask,jsonify,request,abort,render_template,send_from_directory,redirect,url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

PASSKEY = os.getenv('PASSKEY')

if not PASSKEY:
    PASSKEY = input('Set a password for accessing the API endpoints: ')
    with open('.env', 'a') as f:
        f.write(f'PASSKEY={PASSKEY}\n')
    print('Password saved to .env file')

@app.before_request
def check_token():
    if request.endpoint not in ['index', 'download','log']:
        token = request.headers.get('PASSKEY')
        if token != PASSKEY:
            abort(401)

@app.route('/login', methods = ['POST'])
def log():
    data = request.get_json()
    if data['passkey'] == PASSKEY:
        return jsonify({'status':'ok'})
    else:
        return jsonify({'status':'error'})


Folder_input = input('Enter the folder path to serve files from: ')

Folder = Folder_input
os.makedirs(Folder , exist_ok=True)
app.config['Folder'] = Folder

@app.route('/')
def index():
    files = os.listdir(Folder)
    return render_template('index.html' , files=files) 

@app.route('/upload',methods = ['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['Folder'] , file.filename))
    return redirect(url_for('index'))

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(app.config['Folder'] , filename)

@app.route('/api/files')
def json():
    files = os.listdir(Folder)
    return jsonify(files)

@app.route('/delete/<filename>', methods = ['POST'])
def delete(filename):
    file_path = os.path.join(app.config['Folder'], filename)
    os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000 , debug=False)