import hashlib
import random
import string

def make_salt():
    return ''.join([random.choice(string.ascii_letters) for x in range(35)])

def make_pw_hash(salt, password):
    salted_pw = salt + password
    hash = hashlib.sha256(str.encode(salted_pw)).hexdigest()
    return hash

def check_pw_hash(salt, password, hash):
    if make_pw_hash(salt, password) == hash:
        return True
    return False