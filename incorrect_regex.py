'''
prog = re.compile(pattern)
result = prog.match(string)
is equivalent to
result = re.match(pattern, string)

'''

import re

num = int(input())
for _ in range(num):
    curr_regex = input()
    try:
        re.compile(curr_regex)
        print(True)
    except:
        print(False)