#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  October 31, 2022
#This program takes in data from CSV file and prints the Max based Percentage of Country's internet users

import matplotlib.pyplot as plt
import pandas as pd

percent = pd.read_csv('country_internet.csv ')
output = input("Enter output file name: ")

percent['Percentage'] = (percent['Internet users']/percent['Population'])*100
percent.plot(x = 'Country', y = 'Percentage')

maxIdx = percent['Percentage'].idxmax()
print("maximum percentage of all countries: ", percent['Country'][maxIdx],round(percent['Percentage'].max(), 2), "%")

#plt.show()
fig = plt.gcf()
fig.savefig(output)
