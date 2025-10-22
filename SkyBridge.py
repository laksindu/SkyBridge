from flask import Flask,jsonify,request,abort,render_template,send_from_directory,redirect,url_for
from dotenv import load_dotenv
import os
import socket



load_dotenv()

app = Flask(__name__)

PASSKEY = os.getenv('PASSKEY')

PASSKEY = os.getenv('PASSKEY')
FOLDER = os.getenv('FOLDER')
if FOLDER:
    os.makedirs(FOLDER, exist_ok=True)
app.config['Folder'] = FOLDER

@app.before_request
def check_token():
    if request.endpoint not in ['index', 'download','log','admin_ui','setup_status','setup','login_admin','update_settings','get_ip','static','Check_Folder','shutdownfun']:
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

Folder = FOLDER

@app.route('/checkFolder')
def Check_Folder():
    if not FOLDER:
        return jsonify({'status':'no_folder'})
    else:
        return redirect (url_for('index'))

@app.route('/')
def index():
    files = os.listdir(FOLDER)
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
    folder = app.config.get('Folder')
    files = os.listdir(folder)
    return jsonify(files)

@app.route('/delete/<filename>', methods = ['POST'])
def delete(filename):
    file_path = os.path.join(app.config['Folder'], filename)
    os.remove(file_path)
    return redirect(url_for('index'))


FOLDER = os.getenv("FOLDER")


def save_env(key, value):
    """Helper function to update or add a variable in .env"""
    lines = []
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            lines = f.readlines()

    with open(".env", "w") as f:
        found = False
        for line in lines:
            if line.startswith(f"{key}="):
                f.write(f"{key}={value}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"{key}={value}\n")


@app.route("/setup-status")
def setup_status():
    """Tell frontend if setup is done"""
    if not PASSKEY or not FOLDER:
        return jsonify({"status": "not"})
    return jsonify({"status": "ok"})


@app.route("/setup", methods=["POST"])
def setup():
    """First-time setup"""
    data = request.get_json()
    new_pass = data.get("passkey")
    new_folder = data.get("folder")

    global PASSKEY, FOLDER

    if PASSKEY and FOLDER:
        return jsonify({"error": "Already configured"}), 400

    if not new_pass or not new_folder:
        return jsonify({"error": "Missing data"}), 400

    save_env("PASSKEY", new_pass)
    save_env("FOLDER", new_folder)
    PASSKEY = new_pass
    FOLDER = new_folder
    os.makedirs(FOLDER, exist_ok=True)
    return jsonify({"status": "saved"})


@app.route("/login-admin", methods=["POST"])
def login_admin():
    """Login admin"""
    data = request.get_json()
    entered_pass = data.get("passkey")

    if not PASSKEY:
        return jsonify({"error": "Setup not completed"}), 400

    if entered_pass == PASSKEY:
        return jsonify({"check": "ok"})
    return jsonify({"check": "fail"})


@app.route("/update-settings", methods=["POST"])
def update_settings():
    """Update password or folder"""
    global PASSKEY, FOLDER 
    data = request.get_json()
    token = data.get("token")
    if token != PASSKEY:
        abort(401)

    new_pass = data.get("new_pass")
    new_folder = data.get("new_folder")

    if new_pass:
        save_env("PASSKEY", new_pass)
        PASSKEY = new_pass

    if new_folder:
        save_env("FOLDER", new_folder)
        os.makedirs(new_folder, exist_ok=True)
        FOLDER = new_folder

    return jsonify({"status": "updated"})


@app.route("/admin")
def admin_ui():
    """Serve the admin web interface"""
    return render_template("admin.html")


@app.route("/get-ip")
def get_ip():
    import psutil

    # Try to detect the correct local (192.168.x.x) IP
    ip_address = None
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address.startswith("192.168."):
                ip_address = addr.address
                break
        if ip_address:
            break

    # Fallback if not found
    if not ip_address:
        ip_address = request.host.split(':')[0]

    port = request.host.split(':')[1] if ':' in request.host else '80'

    return {'ip': ip_address, 'port': port}


@app.route('/shutdown' , methods = ['POST'])
def shutdownfun():
    import signal
    try:
        shutdown_func = request.environ.get('werkzeug.server.shutdown')
        if shutdown_func:
            shutdown_func()
        else:
            pid = os.getpid()
            os.kill(pid, signal.SIGTERM)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def open_admin_page():
    import webbrowser
    webbrowser.open_new_tab('http://localhost:5000/admin')

if __name__ == '__main__':
    import threading
    threading.Timer(1.5, open_admin_page).start()
    app.run(host='0.0.0.0' , port=5000 , debug=False)