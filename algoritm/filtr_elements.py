# У вас есть данные внутри последовательности, и вы хотите извлечь значения или
# сократить последовательность по какому-либо критерию.
# Самый простой способ фильтрования последовательности –
# использовать генератор списка (list comprehension).

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# Потенциальная проблема с использованием генераторов списков заключается в том,
# что они могут создать большой результат, если размер входных данных
# тоже большой. Если это вас беспокоит, вы можете использовать выражения-генераторы для
# итеративного возврата отфильтрованных значений.

pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# При более сложной логике можно поместить в встроеную функ фильтер

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# Одна из разновидностей фильтрования включает замену значений, которые не
# подходят под определенный критерий, другими значениями (вместо отбраковки
# неподходящих). Например, вместо простого поиска положительных значений вы
# также хотите обрезать «плохие» значения, чтобы они попадали в определенный
# диапазон. В большинстве случаев это легко сделать с помощью перемещения критерия
# фильтрования в условное выражение:

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)