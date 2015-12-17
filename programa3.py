'''comentari'''
from Crypto.Cipher import AES

CLAU = b"1234567898765432"
IV = b"1111111111111111"

OBJ = AES.new(CLAU, AES.MODE_CBC, IV)

MISSATGE = input("Introdueix una frase:")

NUM = len(MISSATGE)
MOD = NUM % 16
if MOD > 0:
    PADDING = 16 - MOD
    MISSATGE += "0" * PADDING

CODIFICAT = OBJ.encrypt(MISSATGE)

print("Missatge original:", MISSATGE[:NUM])
print("Missatge codificat:", CODIFICAT)

OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
DECO = OBJ2.decrypt(CODIFICAT)
print("Missatge descodificat:", DECO[:NUM])
