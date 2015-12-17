'''comentari'''
from Crypto.Cipher import AES

CLAU = b"1234567898765432"
IV = b"1111111111111111"

FILE_IMG = open("gustau.enc", "rb")
FILE_ENC = open("gustau.enc", "wb")
BLOCS = 8192
OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
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
    ENC = OBJ2.decrypt(BLOC)
    FILE_ENC.write(ENC)
FILE_ENC.close()
FILE_IMG.close()
