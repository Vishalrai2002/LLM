import rule_parser, log_analyzer, insights_generator
from utils import file_utils

def main():
    # Load compliance rules from files
    rules = rule_parser.parse_rules(file_utils.read_rule_file('data/compliance_documents/rule_set1.txt'))
    
    # Analyze logs and check for compliance breaches
    log_files = file_utils.get_log_files('data/logs')
    compliance_breaches = log_analyzer.analyze_logs(log_files, rules)
    
    # Generate actionable insights
    insights = insights_generator.generate_insights(compliance_breaches)
    
    # Display or save the insights and results
    for insight in insights:
        print(insight)

if __name__ == "__main__":
    main()
