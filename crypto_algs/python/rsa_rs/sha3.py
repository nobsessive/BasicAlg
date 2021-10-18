import hashlib
cipher = hashlib.sha3_256()
print(cipher.name)
print(cipher.digest_size)

cipher.update("hello".encode(encoding="utf-8"))

# # -- python 3 encoding --
# # string is encoded as Unicode by default
# print('1 >> ----')
# print (type('我好'))
# print(str.encode('''我好'''))
# a=b'\xe6\x88\x91'.decode()
# print(type(a))
# print(a=='我')
# print('1 << ----')

# # str.encode() is used to convert a string to bytes
# print('2 >> ----')
# print("abc".encode(encoding="utf-8"))
# print("abc".encode(encoding="cp037"))
# print('2 << ----')

# chr() is used to convert a Unicode code number to a character
# import unicodedata
# print(chr(int('6211',16))) # 我 is 6211 in hex or 25105 in decimal
# # -- python 3 encoding --



s=cipher.digest()
print(s)

rsa_pub=s+s+s+s+s+s+s+s # repeat eight times to get rsa_pub of 2048 bits


