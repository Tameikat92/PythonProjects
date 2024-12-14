# Starter code
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file
handle = open(name)

# Dictionary to store hour counts
hour_counts = {}

# Process each line in the file
for line in handle:
    # Look for lines that start with 'From '
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Extract the time (5th word)
        time = words[5]
        # Split the time by colon to get the hour
        hour = time.split(':')[0]
        # Increment the count for the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Close the file
handle.close()

# Sort the dictionary by hour (key) and print
for hour, count in sorted(hour_counts.items()):
    print(hour, count)
