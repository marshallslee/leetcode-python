# Date: February 4, 2020 (TUE)
# Link: https://leetcode.com/problems/rotate-array/


def rotate(nums, k):
    tmp_arr = [None] * len(nums)
    for i in range(len(nums)):
        tmp_arr[(i+k) % len(nums)] = nums[i]

    for j in range(len(nums)):
        nums[j] = tmp_arr[j]
    print(nums)
    return


def run():
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    i = 3
    rotate(arr1, i)

    arr2 = [1, 2]
    j = 1
    rotate(arr2, j)
    return


if __name__ == '__main__':
    run()
