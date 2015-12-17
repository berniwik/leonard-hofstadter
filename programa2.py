'''Comentario'''

from Crypto.Cipher import AES

CLAU = b"1234567898765432"
IV = b"1111111111111111"

OBJ = AES.new(CLAU, AES.MODE_CBC, IV)

FITXER = open("fitxer.txt", 'r')
LINIES = FITXER.READLINES()
FITXER.CLOSE()

MISSATGE = ""

for LINIA in LINIES:
    MISSATGE = MISSATGE + LINIA

print(MISSATGE)

NUM = len(MISSATGE)
MOD = NUM % 16
if MOD > 0:
    PADDING = 16 - MOD
    MISSATGE += "0" * PADDING

CODIFICAT = OBJ.encrypt(MISSATGE)

FITXER2 = open("prova.txt", 'w')
FITXER2.WRITE(CODIFICAT)
FITXER2.CLOSE()

print("Missatge original:", MISSATGE[:NUM])
print("Missatge codificat:", CODIFICAT)

OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
DECO = OBJ2.decrypt(CODIFICAT)
print("Missatge descodificat:", DECO[:NUM])
