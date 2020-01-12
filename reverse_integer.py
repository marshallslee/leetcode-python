# Source: https://leetcode.com/problems/reverse-integer/
# Date: Jan 12 (SUN), 2020


def reverse(num):
    str_result = ""
    repeat = len(str(num))

    for i in range(repeat):
        mod = num % 10
        num //= 10
        str_result += str(mod)
    result = int(str_result) * -1
    return result


print(reverse(1203))
