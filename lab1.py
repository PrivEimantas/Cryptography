"""
TASK ONE
"""

def taskOne(stringA,stringB):
    hex1 = int(stringA,16)
    hex2 = int(stringB,16)

    return(hex1^hex2)

def myXOR(data1, data2):
    # Do any required data conversions
    # Perform XORing
    output=taskOne(data1,data2)
    hex_int = hex(output)[2:]
    return(hex_int)
    
    # Hex representation of your result

# Include any required modules
def buildTables(rotationNumber):
    plainToCipher = {}
    cipherToPlain = {}

    # The function should return 2 dictionaries.
    # The dictionaries should keep the mapping of plaintext characters
    # to ciphertext ones and vice versa
    # TODO
    return (plainToCipher, cipherToPlain)
def encrypt(plainText, plainToCipher):

    for i in range(0,len(plainText)):
        plainToCipher[plainText[i]]=i
    # The function should encrypt the plaintext using the
    # plainToCipher dictionary built by the function buildTables
    # TODO
    return #TODO
def decrypt(cipherText, cipherToPlain):
    # The function should decrypt the cipherText using the
    # cipherToPlain dictionary built by the function buildTables
    # TODO
    return #TODO


def XORDecrypt(data):
    # Implement the function
    data = bytearray.fromhex(data)
    print(data[0])
    #Run a loop against all uppercase characters and decrypt and see output
    for i in range(65,91):
        #decrypt for each one
        print(chr(i))
        key = int(bytes(chr(i),'utf-8').hex(),16)
      
        str=""
        for j in range(0,len(data)):
            output = data[j] ^ key
            str+=chr(output)
        print(str)
        print("\n")
        

    return(0)

# Main
if __name__ == "__main__":
    # Task 1.1 Invoke myXOR and print the result
    string1="49276d20746865206b6579212020486f6f72726179212020492063616e20656e637279707421"
    string2="00534d571b1a0e534a452e444c4c680b001c1740597648413d0002410952000f17520e1f064a"
    output=taskOne(string1,string2)
    #print(hex(output))

    # Task 1.2 Print the decoded value of the result
    hex_int = myXOR(string1,string2)
    hex_int_to_bye = bytes.fromhex(hex_int)
    string_value = str(hex_int_to_bye,'utf-8')
    #print(string_value)
    

    """
    TASK TWO
    """
    
   # hex_encoded_string = "16203a6f242120386f3b272a6f242a366f212038636f3d2628273b70"
   # XORDecrypt(hex_encoded_string)

    """
    key: O
    string: You know the key now, right?
    """

    "TASK3"


    """
     1. Create 2 dictionaries using the buildTables function
    using a rotation number, e.g. 10
    2. Create a string with a plaintext, e.g. “hello world!”
    3. Encrypt the plaintext and print the ciphertext
    4. Decrypt the ciphertext and print the plaintext
    
    """
   


