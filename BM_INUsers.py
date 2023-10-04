#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  October 31, 2022
#This program takes in data from CSV file and prints the Max based Percentage of Country's internet users

import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('country_internet.csv')
output = input("Enter output file name: ")

internet['Percentage'] = (internet['Internet users']/internet['Population'])*100
internet.plot(x = 'Country', y = 'Percentage')

print("maximum percentage of all countries: ", internet['Country'].value_counts()[:1], internet['Percentage'].max(), "%")

fig = plt.gcf()
fig.savefig(output)
