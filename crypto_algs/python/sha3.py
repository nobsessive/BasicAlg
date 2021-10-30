import hashlib
cipher = hashlib.sha3_256()
print(cipher.name)
print(cipher.digest_size)


#cipher.update("hello".encode(encoding="utf-8"))
# s=bytes.fromhex('3d389e611a9fc752d47833ad43e5b4dc17dba95bae7aec5d7eab7103a3101188209cd5c013682cad1432e57336bd641ca33e726398006915d7bf88cdeecb5421182536824f7a385ad893552aab80e098241e520bd59ee273d224966bbc789cd9a0bcc76ed76d6d12cf9d2ca1ac55c4a9cc4c56d09c49efb27ed9120e24d7e2c604b8cb1a0c8077ef8bf1e03920396f4a4195d08e5a691f2f89371c6158e961bf848b3a7bd712db52308a51b1982e9c124509d75e2375317f36866b232400c2981ba2dabdbf020d9a010a3b2131abb5af1999aa13026f6e5e03b156ec80400488418c966050b63fe7b4d8042117ecba4388253f5665da3820e87da4a62e1f2b6792c7c93ead380d2907d2152deb08a3313ae795c13201bfcff20e7760ceb9d547b08be2c9c837708c62e5c443a456054904c10e5d646db9c8edb252b6849ba4124d48c09d5f00ce99')
# cipher.update(s)
# print(cipher.hexdigest())

# # --- python 3 string, bytes, and bits ---

# # -- string and bytes --
# 1. string is encoded as Unicode by default
# print('-- string and bytes --1 >> ----')
# print (type('我好'))
# print(str.encode('''我好'''))
# a=b'\xe6\x88\x91'.decode()
# print(type(a))
# print(a=='我')
# print('-- string and bytes --1 << ----')
# 2. str.encode() is used to convert a string to bytes
# print('-- string and bytes --2 >> ----')
# print("abc".encode(encoding="utf-8"))
# print("abc".encode(encoding="cp037"))
# print('-- string and bytes --2 << ----')
# 3. chr() is used to convert a Unicode code number to a character (actually a string)
# import unicodedata
# print(chr(int('6211',16))) # 我 is 6211 in hex or 25105 in decimal
# # -- string and bytes --


# # -- bytes and bits --
# 1. bytes can be converted from and to literal using b'', however, b'1' is not 00000001
# rather it is 31 in hex, since 1 is encoded to 31 in utf-8
import bitstring
print(bitstring.BitArray(bytes=b'1'))
print("1".encode(encoding="utf-8").hex())

# # -- bytes and bits --

# # --- python 3 string, bytes, and bits ---