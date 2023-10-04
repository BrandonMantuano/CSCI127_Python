#Name:  Brandon Mantuano 
#Email: brandon.mantuano45@myhunter.cuny.edu
#Date:  November 12, 2022
#This program creates a map of nyc with a markers for afterschool programs 

import folium
import pandas as pd

AfterSchool = pd.read_csv('after_school.csv')
mapS = folium.Map(location=[40.75, -74.125], zoom_start=10)

print("Enter 1 for Borough/Community, 2 for Grade Level / Age Group")
choice = int(input("Your choice: "))

if choice == 1:
    grouped_data = AfterSchool.groupby('Borough/Community')
    print(grouped_data.groups.keys())

    Community = input("Enter Borough/Community name: ")
    for index,row in grouped_data.get_group(Community).iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapS)

        f = Community.replace('/','_')
        filename = f.lower()
        mapS.save(outfile=filename+"_after_school.html")


if choice == 2:
    grouped_data = AfterSchool.groupby('Grade Level / Age Group')
    print(grouped_data.groups.keys())

    GradeLevel = input("Enter Grade Level / Age Group name: ")
    for index,row in grouped_data.get_group(GradeLevel).iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(mapS)

        f = GradeLevel.replace('/','_')
        filename = f.lower()
        mapS.save(outfile=filename+"_after_school.html")
