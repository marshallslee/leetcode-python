# Date: March 2, 2020 (MON)
# Link: https://leetcode.com/problems/fibonacci-number/


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def run():
    f = fib(2)
    print(f)
    return


if __name__ == '__main__':
    run()
