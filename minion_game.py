def minion_game(string):
    # your code goes here
    length = len(string)
    sub_strings = [string[i:j+1] for i in range(length) for j in range(i, length)]
    vowel_counts = 0
    consonant_counts = 0
    for item in sub_strings:
        if item.startswith(("A","E","I","O","U")):
            vowel_counts += 1
        else:
            consonant_counts += 1
    if vowel_counts > consonant_counts:
        print("Kevin",vowel_counts)
    elif vowel_counts < consonant_counts:
        print("Stuart", consonant_counts)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
