def merge_the_tools(string, k):
    factor = len(string) // k
    for i in range(factor):
        cur_str = string[i*k:i*k+k]
        print(remove_duplicates(cur_str))

def remove_duplicates(string):
    l = list()
    for c in string:
        if c not in l:
            l.append(c)
    return "".join(l)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)