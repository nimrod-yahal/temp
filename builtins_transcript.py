# socket
# You could start by asking them about ways two PCs could communicate
# How would you transfer a file with sockets- very barbaric
# Summarize it is possible but quickly move on to showcase http.server


# HTTP server one-liner from the command-line, useful for file sharing
# python -m http.server
# python -m http.server 80


# Base64, encode binary data as readable text (which is a must over HTTP)
import base64
s = base64.b64encode(b'Aga\x01\x02mim')
print(s)
print(base64.b64decode(s))


# types
import types

def yes_man():
    yield True

print(isinstance(yes_man(), types.GeneratorType))


# random
import random

chosen = random.choice(['A', 'B', 'C', 'Banana'])
print(chosen)

numbers = list(range(10))
random.shuffle(numbers)
print(numbers)


# itertools
import itertools

print(list(itertools.combinations('ABC', 2)))


# defaultdict
from collections import defaultdict

histogram = defaultdict(int)
sentence = 'Hungry like the wolf'
for word in sentence.split():
    histogram[word] += 1 # No need for the 'if word not in histogram ...'

print(histogram)


# Deep copy
from copy import deepcopy

data = {'key_1': {'key_2': 123}}
data_copy = data.copy() # Shallow copy
data_deep_copy = deepcopy(data) # Full copy

data['key_1']['key_2'] = 456
print(data_copy)
print(data_deep_copy)


# json
import json

d = json.loads('{"props": {"id": 1, "value": 5}}')
print(d)


# CSV
import csv

with open('example.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in range(1, 5):
        writer.writerow([i ** j for j in range(1, 4)])

with open('example.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    lines = ['\t'.join(row) for row in reader]
    text = '\n'.join(lines)
    print(text)


# Date and time
from datetime import datetime, timedelta

now = datetime.now()
print(now)

one_week_from_now = now + timedelta(days=7)
print(one_week_from_now)


# Paths
from pathlib import Path

p = Path('result_file')
p.write_text('agamim')
data = p.read_text()
print(data)
p.unlink()

import shutil
shutil.rmtree(Path('/home/guy/family_album'))


# Honorable mentions:
# - argparse
# - urllib: dealing with URLs and making requests
# - re: Regular expressions
# - logging: duh!
# - smtplib: Can send actual mails!
