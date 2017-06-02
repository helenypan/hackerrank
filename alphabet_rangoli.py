import string

def print_rangoli(size):
	letters =string.ascii_lowercase
	arr_len = size + size -1
	index_arr = [None] * arr_len
	index_arr[size - 1] = size
	for i in range(1, size):
		index_arr[size - 1 - i] = size - i
		index_arr[size -1 + i] =  size - i
	
	for i in index_arr:
		row = ["-"] * arr_len
		row[size-1] = letters[size-i]
		for j in range(i):
			row[size-1+j] = letters[size - i + j]
			row[size-1-j] = letters[size - i + j]
		print("-".join(row))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)