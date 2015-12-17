'''comentari'''
from Crypto.Cipher import AES

CLAU = b"1234567898765432"
IV = b"1111111111111111"

OBJ = AES.new(CLAU, AES.MODE_CBC, IV)

MISSATGE = b"missatge origina"

CODIFICAT = OBJ.encrypt(MISSATGE)

print("missatge original:", MISSATGE)
print("missatge codificat:", CODIFICAT)

OBJ2 = AES.new(CLAU, AES.MODE_CBC, IV)
DESCODIFICAT = OBJ2.decrypt(CODIFICAT)
print("Missatge decodificat: ", DESCODIFICAT)
