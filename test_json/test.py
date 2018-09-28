#!/usr/bin/python

import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

str1 = json.dumps(data)
print str1

str2 = json.dumps(data,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))
print str2

dict1 = json.loads(str2)

print dict1
print dict1[0]['a']

