# Date: February 5, 2020 (WED)
# Link: https://leetcode.com/problems/merge-two-sorted-lists/


def merge_two_sorted_lists(l1, l2):
    merged_list = []

    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    merged_list = merged_list + l1[i:] + l2[j:]
    return merged_list


def run():
    list1 = [1, 5, 6, 9, 11]
    list2 = [3, 4, 7, 8, 10]
    n_list = merge_two_sorted_lists(list1, list2)
    print(n_list)
    return


if __name__ == '__main__':
    run()
