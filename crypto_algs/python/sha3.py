import hashlib
cipher = hashlib.shake_128()
print(cipher.name)
print(cipher.digest_size)


#cipher.update("hello".encode(encoding="utf-8"))
s=bytes.fromhex('7C9935A0B07694AA0C6D10E4DB6B1ADD2FD81A25CCB148032DCD739936737F2D')
cipher.update(s)
print(cipher.hexdigest(32))

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
# import bitstring
# print(bitstring.BitArray(bytes=b'1'))
# print("1".encode(encoding="utf-8").   hex())

# # -- bytes and bits --

# # --- python 3 string, bytes, and bits ---