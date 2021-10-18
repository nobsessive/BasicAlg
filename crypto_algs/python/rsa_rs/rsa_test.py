import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
import ast
import hashlib

def read_file(file_name):
    def input_to_hexstring(input_string):
        ret=input_string.replace(":","")
        return ret
    def hex_to_bytes(hex_string):
        return bytes.fromhex(hex_string)
    f=open(file_name,"r")
    s=f.read()
    s=s.replace("\n","")
    s=s.replace(" ","")
    tmp=input_to_hexstring(s)
    tmp=hex_to_bytes(tmp)
    return tmp

cert=read_file("cert.txt")
auth_key_bytes=read_file("auth_key.txt")
import base64
auth_key_b64=base64.b64encode(auth_key_bytes)
auth_key_b64_str=str(auth_key_b64)[2:-1]
pk_const_begin_str="-----BEGIN PUBLIC KEY-----\n"
pk_const_end_str="\n-----END PUBLIC KEY-----"
pub_key=RSA.import_key(pk_const_begin_str+str(auth_key_b64)[2:-1]+pk_const_end_str)



#random_generator = Random.new().read
#publickey = key.publickey() # pub key export for exchange

cipher = PKCS1_v1_5.new(pub_key)
cipher_text= cipher.encrypt(cert)
#message to encrypt is in the above line 'encrypt this message'

print('cipher_text message:', cipher_text) #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(cipher_text)) #write ciphertext to file
f.close()

m = hashlib.sha256()
m.update(b"f65c942fd1773022145418083094568ee34d131933bfdf0c2f200bcc4ef164e3")
digest=m.digest()
print('digest:', digest)