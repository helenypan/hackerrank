def is_leap(year):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return True
	else:
		return False


# year = int(input())
# print(is_leap(year))

# N = int(input())
# l = list()
# l[0] = 5
# print(l)

def count_substring(string, sub_string):
	counter = 0
	sub_len = len(sub_string)
	for i in range(len(string)):
		curr_sub = string[i:i+sub_len]
		if curr_sub == sub_string:
			counter += 1
	return counter


def test_count_substring():
	assert count_substring("ABCDCDC","CDC") == 2