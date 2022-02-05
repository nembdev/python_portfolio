#find two distinct laptops that their combined price == 5000

from csv import reader
o_file = open("laptops.csv")
r_file = reader(o_file)
dataset = list(r_file)
dataset = dataset[1:]

price_to_name = {}

for laptop in dataset:
    if int(laptop[2]) in price_to_name:
        price_to_name[int(laptop[2])].append(laptop[1])
    else: 
        price_to_name[int(laptop[2])] = [laptop[1]]
    

#print(price_to_name)

for laptop in dataset:
    #grab the current price
    price = int(laptop[2])
    #if the price is half of our target cost
    #check for another entry, if > 2 found target
    if price == 2500 and  len(price_to_name[2500]) >= 2:
        laptop1 = price_to_name[price][0] 
        laptop2 = price_to_name[price][1] 
    #another price?
    #search using the remainder
    elif 5000 - price in price_to_name:
        #we know this laptop exists AND the remainder,totaling 5k, exists as well
        #set the first price
        laptop1 = price_to_name[price][0]
        #search and set the second price
        laptop2 = price_to_name[5000 - price][0]
