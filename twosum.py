# Source: https://leetcode.com/problems/two-sum/
# Date: Jan 10 (FRI), 2020
# Assumptions:
# 1. Each input has exactly one solution.
# 2. Each element is unique, i.e. there cannot be the elements with the same values.


class Solution:
    def __init__(self):
        pass

    @classmethod
    def two_sum(cls, nums, target):
        indices = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    indices.append(nums[i])
                    indices.append(nums[j])
                    break
        return indices


def run():
    s = Solution()
    nums = [2, 7, 9, 11]
    target = 9
    indices = s.two_sum(nums, target)
    print(indices)


run()
