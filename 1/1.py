## [1, 2, 3]) → [2, 3, 1]
## [5, 11, 9]) → [11, 9, 5]
## [7, 0, 0]) → [0, 0, 7]
from random import randint

num_count = 0

while True:
    try:
        num_count = int(input("Введите количество случайных чисел (должно быть больше или равно 3): "))
        if num_count >= 3:
            break
        else:
            print("Ошибка: количество должно быть больше или равно 3.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

nums = [randint(0, 9) for _ in range(num_count)]

print("Изначальный список:", nums)

first = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[-1] = first

print("Изменённый список:", nums)