from cryptography.fernet import Fernet as fernet
import base64

def get_key():
    key = fernet.generate_key()
    return base64.b64encode(key).decode()

def encrypt(data, key):
    f = fernet(base64.b64decode(key))
    encrypted = f.encrypt(data)
    return base64.b64encode(encrypted).decode()

def decrypt(data, key):
    f = fernet(base64.b64decode(key))
    decrypted = f.decrypt(base64.b64decode(data))
    return decrypted.decode()
    
