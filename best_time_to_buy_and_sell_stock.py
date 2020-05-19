# May 19, 2020 (TUE)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


def run():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    max_profit = s.maxProfit(prices)
    print(max_profit)


if __name__ == '__main__':
    run()
