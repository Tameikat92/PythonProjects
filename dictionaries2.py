#TODO
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Prompt the user for a file name
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"  # Use default file if no input is given

# Open the file
handle = open(name)

# Initialize an empty dictionary to store sender counts
senders = {}

# Loop through each line in the file
for line in handle:
    # Look for lines that start with 'From '
    if line.startswith('From '):
        words = line.split()
        # The second word in the line is the email address
        email = words[1]
        # Update the dictionary with the sender's email
        senders[email] = senders.get(email, 0) + 1

# Find the sender with the maximum count
max_count = 0
max_sender = None

for sender, count in senders.items():
    if count > max_count:
        max_count = count
        max_sender = sender

# Print the most prolific committer and their count
print(max_sender, max_count)
