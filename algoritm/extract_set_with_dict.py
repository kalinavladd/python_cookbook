# Вы хотите создать словарь, который будет подмножеством другого словаря

# Эту задачу можно легко решить с помощью генератора словаря (dictionary comprehension).

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# Создать словарь всех акций с ценами больше 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Создать словарь акций технологических компаний
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)