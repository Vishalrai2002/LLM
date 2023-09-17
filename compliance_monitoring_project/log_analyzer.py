def analyze_logs(log_files, rules):
    compliance_breaches = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            logs = file.read().splitlines()
        
        for log in logs:
            # Example: Implement compliance checking logic using rules
            # You'll need to customize this logic based on your project's rules and log format
            is_compliant = check_compliance(log, rules)
            if not is_compliant:
                breach = {
                    'log_file': log_file,
                    'log_entry': log,
                    'description': 'Non-compliant activity detected',
                    'recommendation': 'Take necessary action to address the breach'
                }
                compliance_breaches.append(breach)

    return compliance_breaches

def check_compliance(log_entry, rules):
    # Example: Implement compliance checking logic based on rules
    # You'll need to customize this logic based on your project's requirements
    for rule in rules:
        if rule in log_entry:
            return True
    return False
