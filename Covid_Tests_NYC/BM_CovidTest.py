#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  October 21, 2022
#This program takes in data from CSV file and prints the Min,Max,Mean,Median, and Standard Deviation

import matplotlib.pyplot as plt
import pandas as pd

filename = input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
outputfile = input("Enter output name: ")
pop = pd.read_csv(filename)

print("Min:", pop[borough].min())
print("Max:", pop[borough].max())
print("Mean:", round(pop[borough].mean(), 3))
print("Median:", pop[borough].median())
print("Standard Deviation:", round(pop[borough].std(), 3))

pop['Fraction'] = (pop[borough]) / (pop['case_count'])
pop.plot(x = 'date_of_interest', y = 'Fraction')

plt.show()
fig = plt.gcf()
fig.savefig(outputfile)

