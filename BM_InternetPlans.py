#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  October 31, 2022
#This program takes in data from CSV file and prints the Number of internet plans from regions

import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('country_internet.csv')
grouped_data = internet.groupby('Continental region')

print(grouped_data['NO. OF Internet Plans'].mean())

print("possible regions are", grouped_data.groups.keys())
chosen_region = input("choose a region: ")
print("In region", chosen_region)

Place = grouped_data.get_group(chosen_region)

print("number of countries:", Place['Country'].count())
print("maximum number of internet plans: ", Place['NO. OF Internet Plans'].max())
print("minimum  number of internet plans: ", Place['NO. OF Internet Plans'].min())
output = input("Please enter output file name: ")

Place.plot.bar('Country','NO. OF Internet Plans')
plt.gcf().subplots_adjust(bottom=0.25)
plt.xlabel(f"Country in {chosen_region}")
plt.ylabel("NO. OF Internet Plans")

plt.show()
fig = plt.gcf()
fig.savefig(output)
