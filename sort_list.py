'''
The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .
Your task is to sort the table on the th attribute and print the final resulting table.
'''

n, m = tuple(map(int, input().split()))
lst = list()
for _ in range(n):
    lst.append(list(map(int, input().split())))
k = int(input())
s_lst = sorted(lst, key = lambda x:x[k])
for s in s_lst:
    print(" ".join(str(v) for v in s))
