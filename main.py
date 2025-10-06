from flask import Flask,redirect,render_template,send_from_directory,request,abort,jsonify,url_for
import os

app = Flask(__name__)

Folder = 'Folder'
os.makedirs(Folder , exist_ok=True)
app.config['Folder'] = Folder

@app.route('/')
def index():
    files = os.listdir(Folder)
    return render_template('index.html', files=files)

@app.route('/upload' , methods = ['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['Folder'] , file.filename))
    return redirect(url_for('index'))

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(app.config['Folder'] , filename)

@app.route('/api/files')
def json():
    file = os.listdir(Folder)
    return jsonify(file)

@app.route('/delete/<filename>' , methods = ['POST'])
def delelte(filename):
    file_path = os.path.join(app.config['Folder'], filename)
    os.remove(file_path)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000 , debug=False)