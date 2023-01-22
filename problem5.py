# источник
# https://ru.stackoverflow.com/questions/1488103/Как-разбить-числа-от-1-до-n-на-три-множества-так-чтобы-сумма-чисел-в-каждом-был

def generate_sets(n):
    # база индукции
    base = (
        ((), (), ()),
        None,
        ((1, 5, 6), (2, 3, 7), (4, 8)),
        ((1, 5, 9), (2, 6, 7), (3, 4, 8)),
        None,
        ((1, 4), (2, 3), (5,))
    )

    # индукционный шаг
    step = (1, 6), (2, 5), (3, 4)

    bases = base[n % 6]
    if bases is None:
        return None

    start = sum(map(len, bases))
    assert start % 6 == n % 6

    if n < start:
        return None

    def generator(base, step):
        # база индукции
        yield from base
        for m in range(start, n, 6):
            # индукционный шаг
            yield from (m + s for s in step)

    return tuple(generator(b, s) for b, s in zip(bases, step))


def print_sets(num_sets):
    if num_sets is None:
        print(-1)
    else:
        for part in num_sets:
            sets_nums = [str(p) for p in part]
            print(len(sets_nums))
            print(' '.join(sets_nums))
            print()


n = int(input())
num_sets = generate_sets(n)
print_sets(num_sets)
