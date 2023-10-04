#Name: Brandon Mantuano
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date: October 17, 2022
#This program counts the number of words and number of a and b in the words.

words = input("Enter a list of words, separated by a space: ")
SplitW = words.split(" ")

totalW = len(SplitW)
totalA = 0
totalB = 0
for i in SplitW:
    totalA = totalA +(i[-1].count("a"))
    totalB = totalB +(i[-1].count("b"))

print("number of words: ", totalW)
print("number of words ending with a or b: ", totalA + totalB)
print("fraction of words ending with a or b: ", (round((totalA + totalB)/totalW, 2)))


    
