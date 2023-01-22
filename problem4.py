def count_dividers(N):
    count_div = 1  # количество делителей
    divider = 2  # делитель
    while (divider * divider <= N):
        if N % divider == 0:
            count_div = count_div + 1
            d_new = N // divider
            if d_new != divider:
                count_div = count_div + 1

        # следующий делитель
        divider += 1

    count_div += 1

    return count_div

for i in range(1, 11, 1):
    print(i, count_dividers(i))
