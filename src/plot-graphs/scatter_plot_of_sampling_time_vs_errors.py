import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('../log_data.csv')

# Scatter plot of sampling time vs errors
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['time_taken'], df['errors'], alpha=0.5, color='b', label='Time Taken (s) vs Errors')
ax.set_xlabel('Time Taken (s)')
ax.set_ylabel('Errors')
ax.set_title('Scatter Plot of Sampling Time vs Errors')

ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
