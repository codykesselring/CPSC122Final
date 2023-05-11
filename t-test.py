import pandas as pd
from scipy import stats

# Read in the Spotify streaming history data
df = pd.concat([pd.read_json(f) for f in ['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json', 'StreamingHistory3.json']])

# Convert the endTime column to a datetime column
df['endTime'] = pd.to_datetime(df['endTime'])

# Convert the msPlayed column to minutes
df['minutesPlayed'] = df['msPlayed'] / 60000

# Group the data by day of the week
day_group = df.groupby(df['endTime'].dt.day_name())

# Calculate the mean duration of songs played on weekdays and weekends
weekday_mean = day_group.get_group('Monday')['minutesPlayed'].mean()
weekend_mean = day_group.get_group('Saturday')['minutesPlayed'].mean()

# Perform a t-test to determine if the weekday mean is significantly higher than the weekend mean
t_stat, p_value = stats.ttest_ind(day_group.get_group('Monday')['minutesPlayed'], day_group.get_group('Saturday')['minutesPlayed'])

print(p_value)
if p_value < 0.05:
    print("The average duration of songs played on weekdays is significantly higher than the average duration of songs played on weekends.")
else:
    print("There is no significant difference between the average duration of songs played on weekdays and weekends.")
