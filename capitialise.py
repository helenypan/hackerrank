
def capitalize(string):
    list_string = list(string)
    for idx, c in enumerate(list_string):
        if idx == 0:
            list_string[idx] = list_string[idx].upper()
        elif c == " " and idx < len(string) - 1 and list_string[idx+1] != " ":
            list_string[idx+1] = list_string[idx+1].upper()
    return "".join(list_string)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)