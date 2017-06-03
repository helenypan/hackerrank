n = int(input())
s = set(map(int, input().split()))
num_op = int(input())
for _ in range(num_op):
    curr_op = input().split()
    action = curr_op[0]
    if action == "pop" and len(s)>0:
        s.pop()
    elif action == "remove":
        action_num = int(curr_op[1])
        if action_num in s:
            s.remove(action_num)
    elif action == "discard":
        action_num = int(curr_op[1])
        s.discard(action_num)
print(sum(s))