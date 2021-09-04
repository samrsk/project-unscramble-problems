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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_unique_callers_and_recievers(input_list):
  list_callers = []
  list_recievers = []
  for item in input_list:
      list_callers.append(item[0])
      list_recievers.append(item[1])
  set_callers = set(list_callers)
  set_recievers = set(list_recievers)
  return {"callers" : set_callers, "recievers" : set_recievers}


calls_num_list = get_unique_callers_and_recievers(calls)
texts_num_list = get_unique_callers_and_recievers(texts)

caller_set = calls_num_list["callers"]
others_set = calls_num_list["recievers"].union(texts_num_list["callers"].union(texts_num_list["recievers"]))

list_telemarketers = list(caller_set - others_set)

result = sorted(list_telemarketers)
print("These numbers could be telemarketers: ")
for item in result:
    print(item)