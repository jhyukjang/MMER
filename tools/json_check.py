import json
import pdb

with open('./annotations/ek6/ek6_01.json') as f:
    data = json.load(f)


print(data['labels'])
print(len(data['database']))


pdb.set_trace()
