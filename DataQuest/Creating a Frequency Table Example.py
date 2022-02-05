#creating a frequency table from a dataset, ex" AppleStore.csv

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_count = [] #list holds amount of ratings
for rating in apps_data[1:]: # loop through minus header
    #convert string rating to float, append to the list
    rating_count.append(float(rating[5]))

#find the min and max value for making intervals
rat_min = min(rating_count) #0
rat_max = max(rating_count)# 2.9mil

#estimated intervals
#0 - 10k
#10k-100k
#100k-500k
#500k-1m
#1m-5m+

#setup initial table keys using intervals
freq_table = {"0 - 1000": 0, "10k-100k": 0, "100k-500k": 0, "500k-1m": 0, "1m-5m+": 0}

#loop through values and sort into intervals
for rating in rating_count:
    if rating  >= 0 and rating  < 10000:
        freq_table["0 - 1000"] += 1
    elif rating  > 10000 and rating  < 100000:
        freq_table["10k-100k"] += 1
    elif rating  > 100000 and rating  < 500000:
        freq_table["100k-500k"] += 1
    elif rating  > 500000 and rating  < 1000000:
        freq_table["500k-1m"] += 1
    elif rating  > 1000000 and rating  < 5000000:
        freq_table["1m-5m+"] += 1


#double check count for verification
count = 0
for data in freq_table:
    count += freq_table[data]

print(len(rating_count))
print(count)

#print final result
print(freq_table)
