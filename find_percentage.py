def find_percentage():
    n = int(input())
    student_marks = {}
    # _ is like a place holder
    for _ in range(n):
        # *line is to get all the inputs from the second one and save it to the list line
        name, *line = input().split()
        # note how the map is used here. map(function, list)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0 
    count = 0
    for mark in student_marks[query_name]:
        total = total + mark
        count = count + 1
    avg = total/count
    print(format(avg, '.2f'))

find_percentage()