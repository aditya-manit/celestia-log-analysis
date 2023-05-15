import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Add a column for the hour and day of the day
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day

# Create a pivot table with hours as columns and the count of errors as values
pivot_table = df.pivot_table(values='errors', index='day', columns='hour', aggfunc='sum')

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, cmap='YlGnBu')

plt.title('Heatmap of Errors by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Day')
plt.show()
