def number_of_vow_con(string):
    counter_vow = 0
    counter_con = 0
    for i in string:
        if i in ("A", "E", "I", "O", "U"):
            counter_vow += 1
        else:
            counter_con += 1
    return counter_vow, counter_con


def calculate_char(string, is_vow):
    if len(string) ==1:
        return number_of_vow_con(string)[is_vow]
    else:
        substr1 = string[0:len(string)-1]
        return calculate_char(substr1,is_vow) + number_of_vow_con(string)[is_vow]

def minion_game(string):
    # your code goes here
    vowel_counts = calculate_char(string, 0)
    consonant_counts = calculate_char(string, 1)
    if vowel_counts > consonant_counts:
        print("Kevin",vowel_counts)
    elif vowel_counts < consonant_counts:
        print("Stuart", consonant_counts)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


