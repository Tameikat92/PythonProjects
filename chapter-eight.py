
#USE THE INPUT FUNCTION
#open the file
#try and except for file name specifucally
#loop through each line in the file
#remove extra whitespace from each line
#for loop to split and check if ---- 
#the words is in the list
#if youre going to append to add it
#print which is provided


#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
 #print(line.rstrip())

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     # for loop here
#     for word in words: 
#      word = line.split()
#     if not line startswith('But') : continue 
# print(line.rstrip())

# for loop within a for loop
#USE THE INPUT FUNCTION
#open the file
#try and except for file name specifucally
#create an empty list
#loop through each line in the file
#remove extra whitespace from each line
#for loop to split and check if ---- 
#the words is in the list
#if youre going to append to add it
#print which is provided

# Prompt for the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    # Open the file
    fh = open(fname)
except FileNotFoundError:
    print(f"File '{fname}' not found.")
    quit()

# Initialize a count
count = 0

# Process each line in the file
for line in fh:
    # Strip any trailing whitespace from the line
    line = line.rstrip()

    # Check if the line starts with 'From ' (not 'From:')
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Print the email address (second word)
        print(words[1])
        # Increment the count
        count += 1

# Print the count of lines that start with 'From '
print("There were", count, "lines in the file with From as the first word")

