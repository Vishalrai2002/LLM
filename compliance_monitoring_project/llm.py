import openai

api_key = "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"

prompt = "Generate a compliance breach report for the following incident:\n"
prompt += "Log File: log_file1.txt\n"
prompt += "Log Entry: Unauthorized access detected\n"
prompt += "Description: Non-compliant activity detected\n"
prompt += "Recommendation: Take necessary action to address the breach\n"

def generate_compliance_report(prompt, api_key):
    openai.api_key = "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"
    
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=150,  
        stop=None  
    )
    
    return response.choices[0].text.strip()

compliance_report = generate_compliance_report(prompt, api_key)
print(compliance_report)
