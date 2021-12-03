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
    tag = data[-16:]
    cipher = AES.new(scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1), AES.MODE_GCM, nonce=nonce)
    file_out = io.BytesIO()
    file_object = io.BytesIO(data[32+16:-16])
    data = file_object.read(BUFFER_SIZE)
    while len(data) > 0:
        file_out.write(cipher.decrypt(data))
        data = file_object.read(BUFFER_SIZE)
    try:
        cipher.verify(tag)
    except ValueError:
        return None
    return file_out.getvalue()

def main():
    while 1:
        encrypt_or_decrypt = input("Encrypt or decrypt? (e/d): ")
        if encrypt_or_decrypt == "e":
            data = input("Enter data encrypt: ")
            password = input("Enter password: ")
            path = input("Enter path: ")
            encrypted = encrypt(data.encode(), password)
            print("Encrypted data: ", encrypted)
            with open(path, "wb") as file:
                file.write(encrypted)
            break
        elif encrypt_or_decrypt == "d":
            path = input("Enter path: ")
            password = input("Enter password: ")
            with open(path, "rb") as file:
                data = file.read()
            decrypted = decrypt(data, password)
            print("Decrypted data: ", decrypted)
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()