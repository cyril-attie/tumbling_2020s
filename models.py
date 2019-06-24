from hashlib import sha512
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(32), index=True)
  last_name = db.Column(db.String(32), index=True)
  email = db.Column(db.String(120), index=True, unique=True)
  phone_number = db.Column(db.Integer, index=True)
  password_hash = db.Column(db.String(128))

  # def __init__(self, first_name, last_name, email, username, password):
  #   self.id=id_counter
  #   self.first_name=first_name
  #   self.last_name=last_name
  #   self.email=email
  #   self.username=username
  #   self.set_password(password)

  def set_password(self, password):
    self.password_hash=generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

def hash_10_times(password):
  # returns a 10 times hashed password argument
  p=sha512(password)
  for i in range(9):
    p=sha512(p)
  return p

def generate_password_hash(password):
  return hash_10_times(password)

def check_password_hash(password_hash, password):
  return password_hash == hash_10_times(password)


