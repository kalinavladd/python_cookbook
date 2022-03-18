# Вы хотите проводить различные вычисления (например, поиск минимального
# и максимального значений, сортировку) на словаре с данными.

prices = {
    'ACME': 45.23,
    'APL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)
