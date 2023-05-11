import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read in the data from the JSON files and concatenate them
df = pd.concat([pd.read_json(f) for f in ['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json', 'StreamingHistory3.json']])

# Convert the 'endTime' column to datetime format and create a new column for month
df['endTime'] = pd.to_datetime(df['endTime'])
df['month'] = df['endTime'].dt.strftime('%Y-%m')

# Group the data by artist and month, and calculate total listening time
grouped = df.groupby(['artistName', 'month'])['msPlayed'].sum().reset_index()

# Sort the data by total listening time and select the top 10 artists
top_artists = grouped.groupby('artistName')['msPlayed'].sum().sort_values(ascending=False).head(10).index

# Convert the listening time from milliseconds to hours
grouped['hoursPlayed'] = grouped['msPlayed'] / (1000 * 60 * 60)

# Create a pivot table with top artists as rows, months as columns, and total listening time as values
pivot = pd.pivot_table(grouped[grouped['artistName'].isin(top_artists)], values='hoursPlayed', index='artistName', columns='month', aggfunc='sum', fill_value=0)

# Create line charts for each artist
for artist in top_artists:
    plt.plot(pivot.columns, pivot.loc[artist], label=artist)

plt.xlabel('Month')
plt.ylabel('Total listening time (hours)')
plt.title('Top 10 artists by monthly listening time')
plt.xticks(rotation=90)
plt.legend()
plt.show()
