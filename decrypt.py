from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib
import os

chunksize = 256*1024

print("Decrypt")

original_password = input("password: ").encode('utf-8')

key = hashlib.pbkdf2_hmac(hash_name='sha256', password=original_password, salt=b'#3021_@&$', iterations=100000)  #password to hash, 32byte
aes = AES.new(key, AES.MODE_ECB)


filename = input("복호화할 파일명을 입력해주세요 : ")
decrypted_filename = input("복호화 후 저장될 파일명을 입력해주세요 : ")


with open(filename, 'rb') as infile:      #divide file into small chunks to prevent error
    filesize = int(infile.read(16))
    with open( decrypted_filename, 'wb') as outfile:
        while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                break
            outfile.write(aes.decrypt(chunk))
        outfile.truncate(filesize)

print("Done")
