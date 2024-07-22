import os

file_path = os.path.join(os.path.dirname(__file__), "..", "auth.txt")

def verify_email(email):
    try:
        with open(file_path) as f:
            auth = f.readlines() 
            for line in auth:
                if email in line:
                    return True
        return False
    except Exception as e:
        return False