#lab3
import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
import sys

# Include any required modules
def encrypt(key, plainText):
    # Generate an initialisation vector
    # Construct an AES-CTR Cipher object with the given key and
    # randomly generated initialisation vector
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(bytes(plainText,'utf-8')) + encryptor.finalize()
    
    return (cipherText, iv)
def decrypt(key, cipherText, iv):
    # Construct an AES-CTR Cipher object with the given key and
    # iv to decrypt
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    plainText=decryptor.update(cipherText) + decryptor.finalize()

    return (plainText)

def cioPKCS7(data, block_size): # block size in bits
 from cryptography.hazmat.primitives import padding
 padder = padding.PKCS7(block_size).padder()
 padded_data = padder.update(data)
 padded_data += padder.finalize()
 return padded_data

def myPKCS7(data, block_size):
    # TODO: lth is size of data k is size needed..
    #block_Size = 16 in bytes
    data =bytearray(data)
    inputBlockSize = len(data) #lth
    k = block_size
    for i in range(1,129):
        if(inputBlockSize%k==k-i):
            while(len(data)!=block_size):
                amount=k-inputBlockSize

                print(len(data))
                data.append(amount)
                print(data)
            break
            


   # print(data)
    return bytes(data) # padded data in bytes
# Main
if __name__ == "__main__":
    """
    1. Create a key for AES and a plaintext
    2. Encrypt the plaintext and print the result
    3. Decrypt the ciphertext and print the result


    """
    key = os.urandom(32)
    plainText="hello world!"

    cipherText,iv=encrypt(key,plainText)

    pT=decrypt(key,cipherText,iv)
    #print(pT)
    print(myPKCS7(b"a"*13, 16))

    


    print(cioPKCS7(b"a"*13, 128))
    

