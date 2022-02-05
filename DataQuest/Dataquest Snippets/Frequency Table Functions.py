#takes an index number and a list(with header)
#returns a new list with the extracted values
def extract(index_num):
    new_list = []
    for row in apps_data[1:]:
        new_list.append(row[index_num])
    return new_list


#creates a Frequency table from a given list
def freq_table(a_list):
    new_dict = {}
    for value in a_list:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return new_dict

#accepts a index, and a list
#removes the header
#then creates and returns a freq table for that index
def freq_table(index, data_list):
    new_dict = {}

    for row in data_list[1:]:
        value = row[index]
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return new_dict





#takes a dataset(list) and index
#returns a dict freq table
def freq_table(dataset, index):
    #new dict to be returned
    new_set = {}
    #for each datapoint/row
    for app in dataset:
        #is it in the new set already?
        if app[index] in new_set:
            #if so increase count by 1
            new_set[app[index]] += 1
        else:
            #create a new entry, set to 1
            new_set[app[index]] = 1
    #sets the value of each key to the frequency
    for app in new_set:
        new_set[app] = (new_set[app] / len(dataset) ) * 100

    return new_set
