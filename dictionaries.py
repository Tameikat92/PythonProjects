name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email_counts = dict()

for line in handle:
    if line.startswith("From"):
        email = line.split()[1]
        #email = words[1]
        email_counts[email] = email_counts.get(email,0)+1
        handle