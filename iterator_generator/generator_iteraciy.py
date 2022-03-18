# Вы хотите реализовать собственный паттерн итераций, который будет отличаться
# от обычных встроенных функций (таких как range(), reversed() и т. п.).
import itertools
from collections.abc import Iterable

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 10, 1):
    print(n)

# Вы хотите получить срез данных, производимых итератором, но обычный оператор среза не работает.
# Функция itertools.islice() отлично подходит для получения срезов генераторов
# и итераторов.


def count(a):
    while True:
        yield a
        a += 1


c = count(0)
for x in itertools.islice(c, 10, 20):
    print(x)


# У вас есть вложенная последовательность,
# и вы хотите превратить ее в один плоский список значений
# Это легко решается с помощью рекурсивного генератора с инструкцией yield from.

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
# Производит 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
