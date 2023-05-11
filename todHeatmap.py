import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the Spotify listening history from the JSON files
df = pd.concat([pd.read_json(f) for f in ['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json', 'StreamingHistory3.json']])

# Convert the 'endTime' column to a datetime object
df['endTime'] = pd.to_datetime(df['endTime'])

# Create a new column for the hour of day
df['hour'] = df['endTime'].dt.hour

# Create a pivot table to aggregate the listening time by hour of day and day of week
pivot = df.pivot_table(index='hour', columns=df['endTime'].dt.dayofweek, values='msPlayed', aggfunc=np.sum)

# Create a heatmap of the listening time by hour of day and day of week
plt.figure(figsize=(10,6))
plt.title('Listening Habits by Time of Day')
plt.xlabel('Day of Week')
plt.ylabel('Hour of Day')
plt.xticks([0,1,2,3,4,5,6], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.yticks([0,4,8,12,16,20], ['12am', '4am', '8am', '12pm', '4pm', '8pm'])
plt.imshow(pivot, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.show()