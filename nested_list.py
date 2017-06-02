def print_names():
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    print(students)
    min_val = students[0][1]
    second_min = None
    for i in range(len(students)):
        curr_val = students[i][1]
        if curr_val != min_val and (second_min is None or second_min>curr_val):
            second_min = curr_val
    print(second_min)
    names = [s[0] for s in students if s[1] == second_min]
    for name in names.sort():
        print(name)

print_names()