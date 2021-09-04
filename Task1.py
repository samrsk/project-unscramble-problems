"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_phonenumbers(input_list):
    list_of_numbers = []
    for item in input_list:
        list_of_numbers.append(item[0])
        list_of_numbers.append(item[1])
    return set(list_of_numbers)

def get_unique_numbers():
    numbers_in_texts = get_phonenumbers(texts)
    numbers_in_calls = get_phonenumbers(calls)
    unique_numbers = numbers_in_texts.union(numbers_in_calls)
    count = len(unique_numbers)
    return count


text = 'There are ' + `get_unique_numbers()` + ' different telephone numbers in the records.'

print(text)
