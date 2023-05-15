import re
import csv
from datetime import datetime

log_file = '../logs/syslog.1'  # replace with your log file path
csv_file = 'log_data.csv'

header = ['timestamp', 'from_height', 'to_height', 'errors', 'time_taken']
data = []

timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"  # Define the format of your timestamp
timestamps = []  # List to store all timestamps

# Parse the log file
with open(log_file, 'r') as f:
    for line in f:
        # Match log lines with finished sampling headers event
        match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z).*finished sampling headers.*"from": (\d+), "to": (\d+), "errors": (\d+), "finished \(s\)": (\d+\.\d+)', line)
        if match:
            timestamp, from_height, to_height, errors, time_taken = match.groups()
            data.append([timestamp, from_height, to_height, errors, time_taken])
            timestamps.append(datetime.strptime(timestamp, timestamp_format))  # Add the datetime object to the list

# Write structured data to a CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

# Print the minimum and maximum timestamp
print("Minimum timestamp:", min(timestamps))
print("Maximum timestamp:", max(timestamps))
