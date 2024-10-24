# [1, 2, 3]) → [3, 2, 1]
# [5, 11, 9]) → [9, 11, 5]
# [7, 0, 0]) → [0, 0, 7]

from random import randint

nums = [1, 2, 3]

first = nums[0]
for i in range(2, -1, -1): # Идем с конца списка
    nums [2 - i] = nums [i]
nums[2] = first

print(nums)
