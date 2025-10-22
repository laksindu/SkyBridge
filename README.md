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

### Option 1 — Run from source
Make sure you have **Python 3.10+** installed.

```bash
pip install flask python-dotenv
python SkyBridge.py
```
The admin panel will open in your browser

## Option 2 — Run compiled EXE (Windows)
- Download the latest .exe file from Releases
- Run it — SkyBridge will start automatically
- The admin panel will open in your browser

## Option 3 — Run compiled Linux version
- Download the Linux binary from Releases
- Make it executable:
```bash
chmod +x SkyBridge-linux
./SkyBridge-linux
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
