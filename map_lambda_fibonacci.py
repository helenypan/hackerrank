# lambda is a single expression anonymous function ofthen used as an inline function., it is a function
# that has only one line in its body
# teh lambda function cube equals to the def cut(x) as below
cube = lambda x: x ** 3


# def cube(x):
#     return x**3


def cur_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return cur_fib(n-1) + cur_fib(n-2)


def fibonacci(n):
    lst = []
    for i in range(1,n+1):
        lst.append(cur_fib(i))
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))  #cube here means the lambda function