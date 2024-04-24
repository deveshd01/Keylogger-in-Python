import constant

def read_key_log_file():
    with open(constant.txt_file_path, 'r') as f:
        return f.read()

def clear_key_log_file():
    with open(constant.txt_file_path, 'w') as f:
        f.write("")