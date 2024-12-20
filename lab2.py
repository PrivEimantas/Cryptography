import hashlib

def HexBinSHA256(stringToConvert):
    m = hashlib.sha256()
    m.update(bytes(stringToConvert,'utf-8'))
    binValue = m.digest()
    hexValue = m.hexdigest()
    binValue=bin(int(hexValue, 16))[2:]
    #print(binValue),print(hexValue)
    # The function should calculate the SHA256 value of stringToConvert
    # and convert the hex value to its binary representation
    # TODO
    return (hexValue, binValue)

def bruteForcer(string):
    #Build every possible 5 words in lowercase

    print(string)
    from itertools import combinations_with_replacement

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for (a,b,c,d,e) in combinations_with_replacement(alphabets, 5):
        combo=a+b+c+d+e
        
        m = hashlib.sha256()
        m.update(bytes(combo,'utf-8'))
        hexValue = m.hexdigest()
        print(hexValue)
        print("\n")
            





    """
    for a in range(97,123):
        str=""
        str+=chr(a)
        print(str)
        hexValue,binValue=HexBinSHA256(str)
        if(hexValue==string):
            print("word")
            return(1)
        for b in range(97,123):
            str+=chr(b)
            print(str)
            hexValue,binValue=HexBinSHA256(str)
            if(hexValue==string):
                print("word")
                return(1)
            for c in range(97,123):

                str+=chr(c)
                print(str)
                hexValue,binValue=HexBinSHA256(str)
                if(hexValue==string):
                    print("word")
                    return(1)
                for d in range(97,123):
                    str+=chr(d)
                    print(str)
                   # str = str[:3]
                    hexValue,binValue=HexBinSHA256(str)
                    if(hexValue==string):
                        print("word")
                        return(1)
                    
                    for e in range(97,123):
                        str+=chr(e)
                        print(str)
                        str = str[:4]

                        hexValue,binValue=HexBinSHA256(str)
                        if(hexValue==string):
                            print("word")
                            return(1)

                    str = str[:3]
                str = str[:2]
            str = str[:1]
        str = str[:0]
    
    
    """

    return(1)


import hashlib
def avalancheCalculator(string1, string2):
    # TODO
    string1=bytearray(string1,'utf-8')#' '.join('{0:08b}'.format(ord(x), 'b') for x in string1)
    string2=bytearray(string2,'utf-8')#' '.join('{0:08b}'.format(ord(x), 'b') for x in string2)
    count=0
    for i in range(0,len(string1)):
        if(string1[i]!=string2[i]):
            count+=1
    
    return # The avalanche number


# Main
if __name__ == "__main__":
    HexBinSHA256("hello world!")
    """
    1. Create a string, e.g. “hello world!”
    2. Call HexBinSHA256 to calculate its SHA256 value (hex and binary)
    3. Print the values
    """



    #Task1.2
  #  sha256Digested="94f94c9c97bfa92bd267f70e2abd266b069428c282f30ad521d486a069918925"
    #bruteForcer(sha256Digested)

    #Task2
    inputString="Hello World1"
    inputString2="Hello World2"
    avalancheCalculator(inputString,inputString2)

