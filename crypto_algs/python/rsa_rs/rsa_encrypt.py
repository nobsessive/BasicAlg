import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
import ast
import hashlib
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC
from struct import pack

# Crypto is pycryptodome or pycrypto or pycryptodomex 3.10.1
sha3_cipher= hashlib.sha3_256()
sha3_cipher.update(str.encode('''some password''')) #------------------------- modify this line
seed = sha3_cipher.digest()

class PRNG(object):
  def __init__(self, seed):
    self.index = 0
    self.seed = seed
    self.buffer = b""

  def __call__(self, n):
    while len(self.buffer) < n:
        sha3_cipher.update(self.seed + pack("!I", self.index))
        self.buffer += sha3_cipher.digest()
        self.index += 1
    result, self.buffer = self.buffer[:n], self.buffer[n:]
    return result

key = RSA.generate(2048, randfunc=PRNG(seed))
#key = RSA.generate(2048)
f = open('sec_key.pem','wb')
f.write(key.export_key('PEM'))
f.close()

f = open('pub_key.pem','wb')
f.write(key.publickey().export_key('PEM'))
f.close()

cipher = PKCS1_v1_5.new(key)
ciphertext = cipher.encrypt(b'secret message') #------------------------- modify this line
#f=open('ciphertext.bin','wb')  #------------------------- comment this line when decrypting        
#f.write(ciphertext) #------------------------- comment this line when decrypting
#f.close()  #------------------------- comment this line when decrypting


f=open('ciphertext.bin','rb')
ciphertext = f.read()
sentinel = get_random_bytes(16)
m=cipher.decrypt(ciphertext,sentinel)
print(m)