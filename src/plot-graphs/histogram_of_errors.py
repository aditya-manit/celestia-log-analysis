import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Plotting a histogram of errors
fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(df['errors'], bins=20, alpha=0.5, color='g', label='Errors')
ax.set_xlabel('Errors')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram of Errors - Total Data Points: {len(df["errors"])}')

# Adding count labels above the bars
for i in range(len(n)):
    ax.text(bins[i], n[i], str(int(n[i])))

# Set limits for x and y axes
ax.set_xlim([0, df['errors'].max()])
ax.set_ylim([0, n.max()])

ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
