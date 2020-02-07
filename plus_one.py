# DATE: February 7, 2020 (FRI)
# Link: https://leetcode.com/problems/plus-one/


def plus_one(digits):
    carry = 1
    # range(start, stop, step)
    for i in range(len(digits) - 1, -1, -1):

        carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry == 0:
            return digits

    result = []
    result.append(1)
    for i in range(1, len(digits) + 1):
        result.append(digits[i - 1])

    return result


def run():
    lst = [1, 2, 3]
    l = plus_one(lst)
    print(l)
    return


if __name__ == '__main__':
    run()
