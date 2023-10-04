# Name: Brandon Mantuano
# Email: brandon.mantuano45@myhunter.cuny.edu
# Date: November 6, 2022
# Description: This program creates a map of NYC with a marker in Central Park

# Import necessary libraries
import folium  # For creating interactive maps
import pandas as pd  # For handling data from CSV files

# Get the output file name from the user Ex: nyc.html
output = input("Enter output file: ")

# Read the hospital data from a CSV file named 'nyc_hospitals.csv'
hospitals = pd.read_csv('nyc_hospitals.csv')

# Print the list of hospital names from the dataset
print(hospitals["Facility Name"])

# Create a new map centered around NYC with an initial zoom level of 10
mapH = folium.Map(location=[40.75, -74.125], zoom_start=10)

# Loop through the rows in the hospitals dataset and add a marker for each hospital
for index, row in hospitals.iterrows():
    lat = row["Latitude"]  # Get latitude from the dataset
    lon = row["Longitude"]  # Get longitude from the dataset
    name = row["Facility Name"]  # Get the hospital name from the dataset

    # Create a new marker with a popup displaying the hospital name
    newMarker = folium.Marker([lat, lon], popup=name)

    # Add the marker to the map
    newMarker.add_to(mapH)

# Save the map to the specified output file
mapH.save(outfile=output)
