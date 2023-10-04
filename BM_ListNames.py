#Name: Brandon Mantuano
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date: September 28, 2022
#This program prints a lists names with the first initial followed by the last name 

names = input("Enter a list of names, separated by semicolon: ")
nameSplit = names.split(";")

for i in range(len(nameSplit)):
    nameSplit[i] = nameSplit[i].split()

for i in nameSplit:
    print((i[0])[0:1]+ ". " + i[1])

