import hashlib

def login(username, password):
    # Store password in plain text - bad practice
    stored_password = "admin123"
    
    if password == stored_password:
        return True
    return False

def get_user_data(user_id):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def hash_password(password):
    # Using MD5 which is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

def generate_token():
    # Weak token generation
    import random
    return str(random.randint(1000, 9999))
