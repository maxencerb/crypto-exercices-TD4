import hashlib
import os
import io
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

BUFFER_SIZE = 1024 * 1024

def encrypt(data, password):
    salt = os.urandom(32)
    key = scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1)
    file_object = io.BytesIO(data)
    file_out = io.BytesIO()
    cipher = AES.new(key, AES.MODE_GCM)
    file_out.write(salt)
    file_out.write(cipher.nonce)
    data = file_object.read(BUFFER_SIZE)
    while len(data) > 0:
        file_out.write(cipher.encrypt(data))
        data = file_object.read(BUFFER_SIZE)
    file_out.write(cipher.digest())
    return file_out.getvalue()

def decrypt(data, password):
    salt = data[:32]
    nonce = data[32:32+16]
    cipher = AES.new(scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1), AES.MODE_GCM, nonce=nonce)
    file_out = io.BytesIO()
    file_object = io.BytesIO(data[32+16:])
    data = file_object.read(BUFFER_SIZE)
    while len(data) > 0:
        file_out.write(cipher.decrypt(data))
        data = file_object.read(BUFFER_SIZE)
    return file_out.getvalue()

test = encrypt(b"Hello World", "password")
print(decrypt(test, "password"))