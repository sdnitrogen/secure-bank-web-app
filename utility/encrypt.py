import hashlib

def encrypt(password):
        salt = "5gz"
        db_password = password + salt
        h = hashlib.md5(db_password.encode())
        return h.hexdigest()