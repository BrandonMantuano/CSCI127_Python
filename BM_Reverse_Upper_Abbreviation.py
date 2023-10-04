#Name: Brandon Mantuano
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date: September 18, 2022
#This program prints a Reverse, Uppercase, and Abbreviation.
    
phrase = input("input: ")
backW = ""

for c in phrase:
    backW = c+backW

backUpper=backW.upper()
userPhrase = phrase.split(" ")

Abbreviation = ""
for c in userPhrase:
    Abbreviation+=c[:1].upper()
    
print("user reverse: ", backW)
print("user reverse upper: ", backUpper)
print("user abbreviation: ", Abbreviation)



