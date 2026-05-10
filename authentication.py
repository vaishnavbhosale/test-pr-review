import hashlib
import random

def create_user(username, password):
    # MD5 is cryptographically broken
    hashed = hashlib.md5(password.encode()).hexdigest()
    
    # No input validation
    db_query = f"INSERT INTO users VALUES ('{username}', '{hashed}')"
    
    return {"username": username, "password": hashed}

def generate_session_token():
    # Weak random — predictable
    return str(random.randint(10000, 99999))

def verify_password(input_password, stored_password):
    # Timing attack vulnerability
    return input_password == stored_password

def reset_password(email):
    # Token never expires
    token = generate_session_token()
    print(f"Reset link: http://myapp.com/reset?token={token}")
    return token
