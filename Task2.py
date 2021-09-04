"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_unique_phonenumbers(list):
    list_of_numbers = []
    for item in list:
        list_of_numbers.append(item[0])
        list_of_numbers.append(item[1])
    return set(list_of_numbers)

def get_count_totals(input_set):
    total_mins_by_num = {}
    for item in input_set:
        total_time = 0
        for record in calls:
            if record[0] == item or record[1] == item:
                total_time += int(record[3])
        total_mins_by_num[item] = total_time
    return total_mins_by_num

def get_longest_caller(input_set):
    phonenumber = ''
    time = 0
    for item in input_set:
        if input_set[item] > time :
            phonenumber = item
            time = input_set[item]
    return phonenumber, time
    
            
unique_phonenum = get_unique_phonenumbers(calls)
counts_set = get_count_totals(unique_phonenum)
number , time  = get_longest_caller(counts_set)

print(number +" spent the longest time, " + `time`+" seconds, on the phone during September 2016.")





