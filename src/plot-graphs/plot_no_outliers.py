import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import numpy as np

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Calculate the IQR of the time taken
Q1 = df['time_taken'].quantile(0.25)
Q3 = df['time_taken'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_filtered = df[(df['time_taken'] >= lower_bound) & (df['time_taken'] <= upper_bound)]

# Calculate moving average with a window size of 10
df_filtered['time_taken_smooth'] = df_filtered['time_taken'].rolling(window=10).mean()

# Plotting time_taken over timestamp without outliers
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_filtered['timestamp'], df_filtered['time_taken_smooth'], label='Time Taken (s) - No Outliers (Smoothed)')

# Draw a horizontal line representing the median time taken
median = df_filtered['time_taken_smooth'].median()
ax.axhline(median, color='r', linestyle='--', label=f'Median Time Taken: {median:.2f} sec')

# Formatting the x-axis for dates
date_form = DateFormatter("%Y-%m-%d %H:%M:%S")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_tick_params(rotation=45)

ax.set_xlabel('Timestamp')
ax.set_ylabel('Time Taken (s)')
ax.set_title('Time Taken for Sampling Headers Over Time (No Outliers, Smoothed)')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
