import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in the data from the JSON files and concatenate them
df = pd.concat([pd.read_json(f) for f in ['StreamingHistory0.json', 'StreamingHistory1.json', 'StreamingHistory2.json', 'StreamingHistory3.json']])

# Convert the 'endTime' column to datetime format and create a new column for month
df['endTime'] = pd.to_datetime(df['endTime'])
df['month'] = df['endTime'].dt.strftime('%Y-%m')

# Calculate the total hours played per month
total_hours_per_month = df.groupby('month')['msPlayed'].sum() / (1000 * 60 * 60)

# Create a line graph of the total hours played per month
plt.plot(total_hours_per_month.index, total_hours_per_month.values)
plt.xlabel('Month')
plt.ylabel('Total hours played')
plt.title('Total hours played per month')

# Add a linear regression line
x = np.arange(len(total_hours_per_month)).reshape(-1, 1)
y = total_hours_per_month.values.reshape(-1, 1)
reg = LinearRegression().fit(x, y)
plt.plot(x, reg.predict(x), 'r', label='Linear regression')

plt.xticks(rotation=90)
plt.legend()
plt.show()
