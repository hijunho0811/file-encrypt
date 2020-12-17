from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib
import os
from setuptools import setup

# name, description, version등의 정보는 일반적인 setup.py와 같습니다.
setup(name="test_py2xxx",
    description="py2app test application",
    version="0.0.1",# 설치시 의존성 추가
    setup_requires=["py2app"],
    app=["run.py"],
    options={
        "py2app": {
            # PySide 구동에 필요한 모듈들은 포함시켜줍니다.
            "includes": ["PySide.QtCore",
                        "PySide.QtGui",
                        "PySide.QtWebKit",
                        "PySide.QtNetwork",
                        "PySide.QtXml"]
        }
    }
)


Block_Size = 256

chunksize = 256*1024

print("Decrypt")

original_password = input("password: ").encode('utf8')

key = hashlib.pbkdf2_hmac(hash_name='sha256', password=original_password, salt=b'$3kj##agh_', iterations=100000)  #password to hash, 32byte
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
