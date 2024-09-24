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
    
def get_email_users():
    try:
        with open(file_path) as f:
            auth = f.readlines() 
            return [email.strip() for email in auth]
    except Exception as e:
        return []
    
def create_update_list(emails):
    try:
        with open(file_path, "w") as f:
            for email in emails:
                f.write(email + "\n")
        return {"message": "The list of users has been updated"}
    except Exception as e:
        return {"Error": f"The list of users could not be updated: {str(e)}"}