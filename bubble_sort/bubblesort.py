# using Udemy Bubble SORT

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        # starts at 0 and minus i because every item we
        # consider at least one to be sorted
        for j in range(0, len(nums) - 1 - i, 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


if __name__ == "__main__":
    a = [1, 5, 3, 2, 4, 8, 7]
    print(bubble_sort(a))
