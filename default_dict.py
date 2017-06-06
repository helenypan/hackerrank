'''
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but it has one difference:
The value fields' data type is specified upon initialization.
'''

from collections import defaultdict

# solution 1:
# n,m = tuple(map(int,input().split()))
# groups = defaultdict(list) #the value fields data type here is list
# for _ in range(n):
#     groups['A'].append(input())
# for _ in range(m):
#     groups['B'].append(input())
# for item in groups['B']:
#     positions = list()
#     for idx, val in enumerate(groups['A']):
#         if item == val:
#             positions.append(idx)
#     if len(positions) == 0:
#         positions.append(-1)
#     print(" ".join([str(x) for x in positions]))


# solution 2
n, m = map(int,input().split())
dict_a = defaultdict(list)

list_b = []

for i in range(1, n+1):
    dict_a[input()].append(i)

for i in range(m):
    list_b.append(input())

for item in list_b:
    if item in dict_a:
        print(" ".join(map(str,dict_a[item])))
    else:
        print(-1)