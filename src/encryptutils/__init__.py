#!/usr/bin/env python3
from cryptography.fernet import Fernet

def encrypt(string, key=None):
	"""
	Encrypts a string passed as an argument using an optional key(will be randomly generated if left blank, None, or False)
	"""
	if not key:
		key = Fernet.generate_key()
	f = Fernet(key)
	string = bytes(string, encoding="utf-8")
	return(f.encrypt(string))
def decrypt(string):
	"""
	Decrypts a string passed as an argument.
	"""
	string = bytes(string, encoding="utf-8")
	string, key = string.split("\n\n")
	f = Fernet(key)
	return(f.decrypt(string))
def encrypt_file(file, key=None):
	"""
	Encrypts a file passed as an argument(Can be str or pathlib.*) using an optional key(will be randomly generated if left blank, None or False)
	"""
	if not key:
		key = Fernet.generate_key()
	f = Fernet(key)
	with open(file, "rb") as _file:
		contents = _file.read()
		_file.close()
	contents_encrypted = f.encrypt(contents)
	with open(file, "wb") as _file:
		_file.write(key + b"\n\n" + contents_encrypted)
def decrypt_file(file):
	"""
	Decrypts a file passed as an argument(Can be str or pathlib.*)
	"""
	with open(file, "rb") as _file:
		key, contents = _file.read().split(b"\n\n")
	f = Fernet(key)
	contents_decrypted = f.decrypt(contents)
	with open(file, "wb") as _file:
		_file.write(contents_decrypted)

def encrypt_files(files, key=None):
	"""
	Encrypts multiple files passed as an argument(may be a list, tuple, etc.) using an optional key(will be randomly generated if left blank, None or False)
	"""
	if not key:
		key = Fernet.generate_key()
	f = Fernet(key)
	for file in files:
		encrypt_file(file, key)
def decrypt_files(files):
	"""
	Decrypts multiple files passed as an argument(may be a list, tuple, etc.)
	"""
	for file in files:
		decrypt_file(file)
