#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  November 4, 2022
#This function takes in a liquid and size and gives a price

import turtle
t = turtle.Turtle()

def flowerRecursion(t, n):
    if n > 0:
        t.forward(100)
        t.left(105)
        t.forward(52)
        t.left(105)
        t.forward(100)
        t.right(170)
        flowerRecursion(t, n -1)
def main():
    flowerRecursion(t, 10)

if __name__ == '__main__':
   main()
    
