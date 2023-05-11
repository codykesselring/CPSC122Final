import pandas as pd
import matplotlib.pyplot as plt

# Read in the data from the provided JSON files
df = pd.concat([pd.read_json(f) for f in ['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json', 'StreamingHistory3.json']])

# Select the artists to include in the graph
artists = ['Giveon', 'Lana Del Rey', 'Rex Orange County', 'Cage The Elephant', 'Frank Ocean', 'Mac Miller', 'Blxst']

# Filter the data to include only the selected artists
df = df[df['artistName'].isin(artists)]

# Convert the "endTime" field to a datetime object
df['endTime'] = pd.to_datetime(df['endTime'])

# Group the data by artist and month, and calculate the total playtime for each month
monthly_playtime = df.groupby(['artistName', pd.Grouper(key='endTime', freq='M')])['msPlayed'].sum() / 3600000  # Convert from milliseconds to hours

# Plot the data for each artist on a line graph
for artist in artists:
    artist_data = monthly_playtime[artist]
    artist_data.plot(label=artist)

# Set the title and axis labels for the graph
plt.title('Monthly Playtime for Selected Artists')
plt.xlabel('Month')
plt.ylabel('Total Playtime (hours)')

# Show the legend and display the graph
plt.legend()
plt.show()