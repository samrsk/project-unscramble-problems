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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_rec_texts = texts[0]
first_rec_calls = calls[0]

print("First record of texts, "+ first_rec_texts[0]+ " texts " + first_rec_texts[1] + " at time " + first_rec_texts[2])
print("First record of calls, "+ first_rec_calls[0]+ " texts " + first_rec_calls[1] + " at time " + first_rec_calls[2] + ", lasting " + first_rec_calls[3] + " seconds")