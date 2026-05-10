import subprocess

def process_payment(user_input):
    # SQL injection vulnerability
    query = "SELECT * FROM payments WHERE id = " + user_input
    
    # Command injection vulnerability  
    result = subprocess.call(user_input, shell=True)
    
    # Hardcoded credentials
    api_key = "sk-prod-1234567890abcdef"
    secret = "supersecretpassword123"
    
    return result
