# Source: https://leetcode.com/problems/reverse-integer/
# Date: Jan 12 (SUN), 2020


def reverse(num):
    result = 0
    original_num = num

    if original_num < 0:
        num *= -1
    else:
        pass

    for i in range(len(str(num))):
        mod = num % 10
        num //= 10
        result = result * 10 + mod

    if original_num < 0:
        result *= -1

    if result > 2 ** 31 or result < -(2 ** 31):
        return 0

    return result


print(reverse(1534236469))
