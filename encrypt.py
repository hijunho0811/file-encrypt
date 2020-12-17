from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget

Block_Size = 256

chunksize = 256*1024

print("Encrypt")

original_password = input("password: ").encode('utf8')
key = hashlib.pbkdf2_hmac(hash_name='sha256', password=original_password, salt=b'$3kj##agh_', iterations=100000)  #change password to 32byte key using hashlib

filename = input("암호화할 파일명을 입려해주세요: ").encode("utf8")
encrypted_filename = input("암호화 후 저장될 파일명을 입력해주세요: ")
turn = 0


filesize = str(os.path.getsize(filename)).zfill(16)  #read file size for decrypting, file size is stored in 16bytes

aes = AES.new(key, AES.MODE_ECB)

with open(filename, 'rb') as infile:         #to prevent error, divide file into chunks
    with open( encrypted_filename , 'wb') as outfile:
        outfile.write(filesize.encode('utf-8'))
        while True:
            chunk = infile.read(chunksize)   #read file
            if len(chunk) == 0:              #break loop after file is fully read
                break
            elif len(chunk) % 16 != 0:       #if last chunk is not 16bytes, input '_' to fill 16 bytes
                chunk += b'_' * (256 - (len(chunk) % 256))
            outfile.write(aes.encrypt(chunk))
