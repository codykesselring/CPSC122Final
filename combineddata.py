import json

# Open the files and load the JSON data
with open('StreamingHistory0.json', encoding='utf-8') as file:
    data0 = json.load(file)
with open('StreamingHistory1.json', encoding='utf-8') as file:
    data1 = json.load(file)
with open('StreamingHistory2.json', encoding='utf-8') as file:
    data2 = json.load(file)
with open('StreamingHistory3.json', encoding='utf-8') as file:
    data3 = json.load(file)

# Combine the data from all four files into a single list
data = data0 + data1 + data2 + data3

# Create a dictionary to store the total msPlayed for each artist
totals = {}

# Loop through each item in the data and add the msPlayed to the artist's total
for item in data:
    artist = item['artistName']
    ms_played = item['msPlayed']
    if artist in totals:
        totals[artist] += ms_played
    else:
        totals[artist] = ms_played

# Sort the artists in descending order by total msPlayed
sorted_artists = sorted(totals, key=totals.get, reverse=True)

# Write the results to a file
with open('outputfile.txt', 'w') as file:
    for artist in sorted_artists:
        file.write(f"{artist}: {totals[artist]}\n")