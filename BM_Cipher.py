#Name: Brandon Mantuano
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date: September 18, 2022
#This program prints a Cipher.
    
phrase = input("Enter all-small-letter string: ")
num = input("Enter a non-negative int to shift: ")
num1 = int(num)

cipher = ""

for ch in phrase:
    if ord(ch)+ num1 <=122:
        cipher += chr(ord(ch)+num1)
    else:
        cipher+=chr(97+(ord(ch)+num1-123))


print("ciphered string:", cipher)

