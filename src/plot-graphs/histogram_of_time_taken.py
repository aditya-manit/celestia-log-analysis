import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Plotting a histogram of time taken
fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(df['time_taken'], bins=20, alpha=0.5, color='r', label='Time Taken (s)')
ax.set_xlabel('Time Taken (s)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram of Time Taken - Total Data Points: {len(df["time_taken"])}')

# Adding count labels above the bars
for i in range(len(n)):
    ax.text(bins[i], n[i], str(int(n[i])))

ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
