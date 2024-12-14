#TODO
#Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.




#  from txt file pull out the hour from the 'From ' line
#by finding the time and then splitting the string a second time
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_count = {} #we can also use dict()

#loop thru eachline in the text file
for line in handle:
    if line.startswith("From"):
        words = line.split() #splitting line into words
        # extract the time part and split
        time = words[5]
        hour = time.split(":")[0]

        # update the hour count in dict
        hour_count[hour] = hour_count.get(hour,0) + 1

for hour, count in sorted(hour_count.items()):
    print(hour,count)
        
     
        






