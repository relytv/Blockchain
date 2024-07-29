import hashlib

def hash256(s):
    """Два раунда sha256"""
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()