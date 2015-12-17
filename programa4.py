'''comentari'''
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

CLAU = b'1234567890123456'

OBJH = SHA256.new(CLAU)
RESUM = OBJH.digest()

IV = b"1111111111111111"

print(OBJH.hexdigest())

FILE_IMG = open("gustau.jpg", "rb")
FILE_ENC = open("gustau.enc", "wb")

BLOCS = 8192
OBJ = AES.new(RESUM, AES.MODE_CBC, IV)
BLOC = 0
while True:
    BLOC = FILE_IMG.read(BLOCS)
    if not BLOC:
        break
    NUM = len(BLOC)
    MOD = NUM % 16
    if MOD > 0:
        PADDING = 16 - MOD
        BLOC += b"0"*PADDING
    ENC = OBJ.encrypt(BLOC)
    FILE_ENC.write(ENC)
FILE_ENC.close()
FILE_IMG.close()
