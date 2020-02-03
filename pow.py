# DATE: February 3, 2020 (MON)
# Source: https://leetcode.com/problems/powx-n/


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        if -100.0 < x < 100.0:
            if n == 0:
                return 1

            if n % 2 == 0:
                tmp = self.my_pow(x, n / 2)
                return tmp * tmp

            if n > 0:
                return x * self.my_pow(x, n - 1)

            # if n is positive, return x * x^(n+1)
            return 1.0 / x * self.my_pow(x, n + 1)
        else:
            print('unable to calculate. x must be between -100.0 and 100.0.')


if __name__ == '__main__':
    s = Solution()
    print(s.my_pow(2.0000, 10))  # Expects 1024
    print(s.my_pow(2.10000, 0))  # Expects 1
    print(s.my_pow(2.1, 3))
    print(s.my_pow(2.0000, -3))  # Expects 0.125
    print(s.my_pow(-10, 2))  # Expects 100

