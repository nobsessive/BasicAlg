'''
Openssl command flow (after generating public and private keys):
openssl pkeyutl -encrypt -pubin -inkey test_public_key.pem -in message.txt -out encrypted_message.bin
openssl pkeyutl -decrypt -inkey test_private_key.pem -in encrypted_message.bin -out decrypted_message.txt

'''


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat

# Load or generate your RSA keys (replace this with your own keys)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Convert the private key to a .pem file
private_pem = private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

# Convert the public key to a .pem file
public_pem = public_key.public_bytes(
    encoding=Encoding.PEM,
    format=PublicFormat.SubjectPublicKeyInfo,
)

# Save the private key to a file
with open('test_private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_pem)

# Save the public key to a file
with open('test_public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_pem)
