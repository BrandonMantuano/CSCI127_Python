#Name: Brandon Mantuano
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date: October 2, 2022
#This program convets centimeters to feet and inches and convets feet and inches to centimeters.

letter = input("Enter a or b or c: ")


if letter == "a":
    centi = int(input("Enter height in centimeters: "))
    result = round(centi/30.48, 2)
    print("height is", result, "feet")
    
elif letter == "b":
        centi = int(input("Enter height in centimeters: "))
        feet = round(centi//30.48)
        inches = round((centi - feet*30.48)/2.54)
        if inches != 0:
            print("height is", feet, "feet and", inches, "inches")
        else:
            print("height is", feet, "feet")
    
elif letter == "c":
    feet_str, inches_str = input("Enter height in feet and inches, separated by a space: ").split()
    feet = int(feet_str)
    inches = int(inches_str)
    result = round((feet*30.48) + (inches*2.54), 0)
    print("height is", result, "cm")
    
else:
    print("Wrong choice, please enter only a or b or c.")
