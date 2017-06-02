def calculate_char(string):
    vow_count, con_count = 0,0
    counter_vow = 0
    counter_con = 0
    for idx in range(len(string)):
        if string[idx] in ("A", "E", "I", "O", "U"):
            counter_vow += 1
        else:
            counter_con += 1
        vow_count += counter_vow
        con_count += counter_con
    return vow_count,con_count

def minion_game(string):
    # your code goes here
    vowel_counts,consonant_counts = calculate_char(string)
    if vowel_counts > consonant_counts:
        print("Kevin",vowel_counts)
    elif vowel_counts < consonant_counts:
        print("Stuart", consonant_counts)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


