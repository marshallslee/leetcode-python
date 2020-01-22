# DATE: January 22, 2020 (WED)
# Source: https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if x > 0:
            for i in range(n):
                result *= x
        elif x == 0:
            result = 1
        else:
            n *= -1
            for i in range(n):
                result //= x
                print(result)
        return format(result, '.5f')


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.0000, 10))
    print(s.myPow(2.10000, 0))
    print(s.myPow(2.0000, -3))
