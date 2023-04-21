import json
from collections import defaultdict
import pprint

f = open('Dataset2/log_human_readable.txt')
  
# returns JSON object as 
# a dictionary
def get_animal(line):
    parts = line.split('-')
    key = int(parts[1][:2])

    ani = None
    if "Elephant" in line:
        ani = "E"
    elif "Zebra" in line:
        ani = "Z"
    elif "Lion" in line:
        ani = "L"

    return ani, key

#animal -> key -> time -> type -> value
record = defaultdict(lambda: 
                     defaultdict(lambda: 
                                 defaultdict(lambda: 
                                             defaultdict(lambda: 
                                                         defaultdict(lambda: None)))))

for j in range(36873):
    head = f.readline()
    ani, key = get_animal(head)
    f.readline()
    time = f.readline()
    f.readline()
    pox = f.readline()
    f.readline()
    loc = f.readline()
    f.readline()
    temp = f.readline()
    f.readline()
    hum = f.readline()
    f.readline()

    record[ani][key][time]['pox'] = pox
    record[ani][key][time]['loc'] = loc
    record[ani][key][time]['temp'] = temp
    record[ani][key][time]['hum'] = hum

for a in record:
    for k in record[a]:
        for t in record[a][k]:
            for v in record[a][k][t]:
                print(a,k,v, record[a][k][t][v])


