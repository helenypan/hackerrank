'''
any(): returns True if any element of the iterable is true: any([1>0,1==0,1<0]) returns True
all(): returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
all(['a'<'b','b'<'c']) returns True
'''


n = int(input()); arr = input().split()
con1 = []; con2 =[]
for num in arr:
    con1.append(int(num) > 0)
    # str(num) == str(num)[::-1] : to check it this num is a palindrome
    con2.append(str(num) == str(num)[::-1])
print(all(con1) and any(con2))