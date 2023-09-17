from flask import Flask, render_template, request
from utils import file_utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_rules_endpoint', methods=['POST'])
def upload_rules():
    rule_file = request.files['ruleFile']
    if rule_file:
        rule_content = rule_file.read().decode('utf-8')
        rule_text = file_utils.read_rule_file(rule_content)
        
        
        return 'Rule file uploaded successfully'

    return 'No rule file uploaded'

@app.route('/upload_logs_endpoint', methods=['POST'])
def upload_logs_endpoint():
    if 'logFiles' not in request.files:
        return "No files were uploaded", 400

    log_files = request.files.getlist('logFiles')
    upload_directory = 'data/logs/'

    file_utils.save_uploaded_logs(log_files, upload_directory)

    
    
    return "Log files uploaded successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
