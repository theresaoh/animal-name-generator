import hashlib
import random
import string

def make_salt():
  # randomly generate a salt for each user
  return ''.join([random.choice(string.ascii_letters) for x in range(35)])

def make_pw_hash(salt, password):
  # add salt to password and hash the entire thing
  salted_pw = salt + password
  hash = hashlib.sha256(str.encode(salted_pw)).hexdigest()
  return hash

def check_pw_hash(salt, password, hash):
  # verify that the password entered by a user on login is the same as the secure pass in the db
  return make_pw_hash(salt, password) == hash
