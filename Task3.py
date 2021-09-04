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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_recivers_from_caller(caller_pattern):
  list_numbers = []
  for item in calls:
    if caller_pattern in item[0]:
      list_numbers.append(item[1])
  return list_numbers

def get_codes(input_list):
  list_codes = ['']
  for item in input_list:
    if ' ' in item:
      list_codes.append(item[0:5])
    elif '(' in item and '(080)' not in item:
      index = item.find(')')
      list_codes.append(item[1:index])
  return list_codes

def get_calls_to_bangalore_count(input_list):
  count = 0
  for item in input_list:
    if '(080)' in item:
      count += 1
  return count


recievers = get_recivers_from_caller('(080)')
unique_recievers = list(set(recievers))
codes = get_codes(unique_recievers)
unique_codes = list(set(codes))
unique_codes.sort()
print("The numbers called by people in Bangalore have codes:")
for x in unique_codes:
  print(x)

bangalore_recievers_count = get_calls_to_bangalore_count(unique_recievers)
total_calls = len(recievers)
percentage = (float(bangalore_recievers_count) / float(total_calls)) * 100

print("{:.2f}".format(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")