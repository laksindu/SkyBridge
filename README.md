# SkyBridge — Open Source Local File Server

SkyBridge is a lightweight **Flask-based file server** that lets you use any computer — even old ones — as a simple file server accessible from any device on your local network.

---

## Features

- Easy setup via web interface  
- Password-protected admin panel  
- Upload, download, and manage files  
- Change folder and password anytime  
- Works on Windows & Linux  
- Access from any device on your LAN  
- Auto-opens the admin UI at `http://localhost:5000/admin`

---

## Installation

## Option 1 — Run from source
## Windows setup
Make sure you have **Python 3.10+** installed.

```bash
pip install flask python-dotenv
python SkyBridge.py
```
The admin panel will open in your browser

## Linux Setup
Python 3.10 or newer

Check your Python version:
```bash
python3 --version
```

if needed:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
## Step-by-Step Setup
1. Download the project

If using Git:
```bash
git clone https://github.com/your-username/SkyBridge.git
cd SkyBridge
```
Or extract the .zip and open the folder in terminal.

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install flask python-dotenv
```
4. Run the ap
```bash
python SkyBridge.py
```

SkyBridge will start and open the admin panel at:
`http://localhost:5000/admin`


## Option 2 — Run compiled EXE (Windows)
- Download the latest .exe file from Releases
- Run it — SkyBridge will start automatically
- The admin panel will open in your browser

## Option 3 — Run compiled Linux version
- Download the Linux binary from Releases
- Make it executable:
```bash
chmod +x SkyBridge_linux
./SkyBridge_linux
```
Open your browser → http://localhost:5000/admin

## Configuration
All configuration is stored in the .env file:
```bash
PASSKEY=your_admin_password
FOLDER=your_shared_folder_path
```
You can change these anytime via the Admin Settings page.

## How It Works
SkyBridge runs a Flask web server on your computer that lets you:
- Host a folder as a simple local file server
- Access and manage files via a clean web interface
- Secure it with a passkey
- Restart or shut down from the admin panel

## Use Case Ideas
- Turn old PCs or laptops into private file servers
- Share files across your home network
- Use as a mini LAN drive

## Notes
- Ensure devices are on the same local network
- Transfer speed depends on local network performance and your storage device read/write speed
- Currently supports files up to approximately 1.5 GB
- Only one file can be transferred at a time

## Build It Yourself (Developers)
```bash
//Windows
pip install flask python-dotenv pyinstaller
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" SkyBridge.py

//Linux 
pip install flask python-dotenv pyinstaller
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" SkyBridge.py
```

## License
This project is open-source and available under the MIT License.

## Author
- Developed by Laksindu Janith
- Made with Python + Flask
