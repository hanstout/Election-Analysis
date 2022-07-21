from atexit import register


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict['county'])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county} county has {voters:,} registered voters.")



import csv 

file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
     print(election_data)

file_reader = csv.reader(election_data)
for row in file_reader:
        print(row)

import os
dir(os)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")
