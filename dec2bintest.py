#!/usr/bin/python3

#MY TEST
#a = int(input("Type number ")) 
#print (a)
#c =int(a / 2)
#print (c)
#if (c != 0):
#    d = a % 2
#    print (d)

#IT WORKSSS
def dec2bin(num):
    if num > 1:
        dec2bin(num // 2)
    print(num % 2,end = "")
#makes bin number to apper on the left side of the code line - , end =" ")
if __name__ == '__main__':
#type the below decimal number you want to convert
    dec_val =115
# call the fnction
    dec2bin(dec_val)

#https://www.geeksforgeeks.org/program-decimal-binary-conversion/

