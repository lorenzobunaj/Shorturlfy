from cryptography.fernet import Fernet
from utils.conf import CONF

static_key = CONF["SECURE_KEY"]

# encrypt function
def encrypt(url):
    return Fernet(static_key).encrypt(url.encode()).decode()

# decrypt function
def decrypt(url):
    return Fernet(static_key).decrypt(url.encode()).decode()