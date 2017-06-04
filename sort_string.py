'''
to sort the string  in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''

s = input()
s = sorted(s, key = lambda x: (x.isdigit() and int(x)%2 == 0, x.isdigit() , x.isupper(), x.islower(), x))
print(*s, sep="")