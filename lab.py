import sys
import binascii

def strxor(a,b): #xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x)^ord(y)) for(x,y) in zip(a[:len(b)] , b)])
    else:
        return "".join([chr(ord(x)^ord(y)) for(x,y) in zip(a, b[:len(a)])])

with open('input', 'r') as myfile:
    data=myfile.readlines()
    message1 = binascii.unhexlify(data[0])
    message2 = binascii.unhexlify(data[1])

#print(message1)
#print(message2)

#message1xor2 = strxor(message1, message2)
#print(message1xor2)