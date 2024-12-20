# week14lab

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib
# Include any required modules
def doRSA():
 # do RSA
 private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024,
 )
 public_key = private_key.public_key()
 
 pemPriv = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
 )
 pemPriv.splitlines()[0]

 pemPb = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
 )
 pemPb.splitlines()[0]
 return (public_key, private_key)

def task2():
 private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024,
 )
 public_key = private_key.public_key()
 message = b"test"
 ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
 




 
# Main
if __name__ == "__main__":
 #doRSA()
 #Call doRSA to return the public and private keys
  task2()