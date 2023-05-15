import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plotting time_taken over timestamp
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df['timestamp'], df['time_taken'], label='Time Taken (s)')

# Formatting the x-axis for dates
date_form = DateFormatter("%Y-%m-%d %H:%M:%S")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_tick_params(rotation=45)

ax.set_xlabel('Timestamp')
ax.set_ylabel('Time Taken (s)')
ax.set_title('Time Taken for Sampling Headers Over Time')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
