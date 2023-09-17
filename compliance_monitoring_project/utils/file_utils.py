import os

def read_rule_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def get_log_files(directory_path):
    log_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.txt', '.csv')):
                log_files.append(os.path.join(root, file))
    return log_files
