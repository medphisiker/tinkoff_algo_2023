# источник исходного подхода к решению задачи
# https://www.geeksforgeeks.org/count-elements-in-the-given-range-which-have-maximum-number-of-divisors/

# решение с максимальным размером данных (limit = 100000)
# уложилось по памяти и времени работы:
# Компилятор	Python3 3.10.6
# Время, сек	0.127
# Память, МБ	21.87
# Результат	OK

# Отлично, принимаем на ввод limit, убираем эмуляции ответа,
# Отдаем полученный результат

# limit = 100000
limit = int(input())

# массив для хранения числа делителей
arr = [0] * (limit)

# перебор
k = 1
while k * k <= limit:
    sq = k * k

    # найдем первое делимое число
    if ((1 // k) * k >= 1):
        first_num = (1 // k) * k
    else:
        first_num = (1 // k + 1) * k

    # посчитаем число делителей
    for num in range(first_num, limit + 1, k):
        if num < sq:
            continue
        elif num == sq:
            arr[num - 1] += 1
        else:
            arr[num - 1] += 2
    k += 1

# ищем максимальное число с максимальным числом делителей
max_div = 0
max_num = 0

n = 1
for num in arr:
    if num >= max_div:
        max_div = num
        max_num = n

    n += 1

print(max_num)
print(max_div)
