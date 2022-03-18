# Вы хотите создать список N максимальных или минимальных элементов коллекции.
# У модуля heapq есть две функции, nlargest() и nsmallest(), которые делают именно
# то, что вам нужно. Например:

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(5, nums))  # [-4, 1, 2, 2, 7]

# Обе функции также принимают параметр key, который позволяет использовать
# их с более сложными структурами данных. Например:

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)
