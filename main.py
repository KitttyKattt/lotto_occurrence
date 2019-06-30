#!/usr/bin/env python3.7
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
from collections import Counter
import re
import csv
import os

PAGENUMBER = 1
LOTTODATA = []
OFFICIALDATA = {}
NUMBERS = []
TIMES = []
mergedlist = []
CHANCE = []

#uniq numbers 
uniqList1 = []
uniqList2 = []
uniqList3 = []
uniqList4 = []
uniqList5 = []
uniqList6 = []

zc = 0

while PAGENUMBER <= 12:  # Our way of filtering through pages
    COUNTER = 1  # We will need this later
    url = urlopen('http://lotto-centrum.com/lotto/wygrane.php5?data=2018-' + str(PAGENUMBER))
    PAGENUMBER += 1
    RAW = url.read()  # Reads data into variable
    url.close()  # Closes connection
    # print(RAW)
    PARSED = Soup(RAW, 'html.parser')  # (DATA, Type of Parser)
    # print(PARSED)
    for line in PARSED.findAll('table', {'class': 'wyniki'}):  # Finds all the 'td' tags with align:right
        if '<tr>' in str(line):  # Needs to be setup this long way
            pRAW = re.findall(r'\d+', str(line))            
            # print(pRAW[1:])

            LOTTODATA.append(pRAW[1:])
            # for pline in pRAW[1:]:

with open('lotto.csv', 'w') as data:
    file = csv.writer(data)
    file.writerows(LOTTODATA)


i = 0
if os.path.exists("occurrence.csv"):
  os.remove("occurrence.csv")
else:
  print("The file does not exist")

while i < len(LOTTODATA):
  LOTTOLIST = list(LOTTODATA[i])
#   print(LOTTOLIST)
  mergedlist.extend(LOTTOLIST)
  BUFFED = []  # Local list to manipulate
  for line in mergedlist:

    buffer = line.split()
    for bbuffer in buffer:
            BUFFED.append(bbuffer)
    STORED = Counter(BUFFED)  # Counts each unique number
    zc = len(STORED)  # Used to tell us how unique numbers there are
    # print(STORED)
    
  i += 1

  with open('occurrence.csv', 'w') as data:
    file = csv.writer(data)
    file.writerows(STORED.items())

def most_popular_num(lst):
    return max(set(lst), key=lst.count)

file=open("lotto.csv", "r")
reader = csv.reader(file)
for line in reader:
    t=line[0], line[1], line[2], line[3], line[4], line[5]
    # print(t)

    uniqList1.append(line[0])
    uniqList2.append(line[1])
    uniqList3.append(line[2])
    uniqList4.append(line[3])
    uniqList5.append(line[4])
    uniqList6.append(line[5])
i = 0
while i < 1:
  i+=1

mergedNumber = "You must bet on this numbers: " + most_popular_num(uniqList1) + " " + most_popular_num(uniqList2) + " " + most_popular_num(uniqList3) + " " + most_popular_num(uniqList4) + " " + most_popular_num(uniqList5) + " " + most_popular_num(uniqList6)
print(mergedNumber)