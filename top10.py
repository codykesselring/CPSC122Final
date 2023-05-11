import matplotlib.pyplot as plt

# Open the file and read the data
with open('outputfile.txt', 'r') as f:
    lines = f.readlines()

# Parse the data into two lists: names and hours played
names = []
hours = []
for line in lines:
    parts = line.strip().split(': ')
    name = parts[0].replace('$', '\$')
    ms = int(parts[1])
    hours_played = ms / (1000 * 60 * 60)
    names.append(name)
    hours.append(hours_played)

# Sort the names and hours lists in descending order by hours played
sorted_data = sorted(zip(hours, names), reverse=True)[:10]
hours, names = zip(*sorted_data)

# Create the bar graph
plt.bar(names, hours)
plt.xticks(rotation=90)
plt.xlabel('Names')
plt.ylabel('Hours played')
plt.title('Top 10 artists by hours played')
plt.show()
