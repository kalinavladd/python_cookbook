# У вас есть список словарей, и вы хотите отсортировать записи согласно одному
# или более значениям.

# Сортировка структур этого типа легко выполняется с помощью функции itemgetter
# из модуля operator. Предположим, вы выполнили запрос к таблице базы данных,
# чтобы получить список зарегистрированных пользователей вашего сайта, и получили в ответ вот такую структуру данных:

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
# Функция itemgetter() также может принимать несколько ключей.
rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
for line in rows_by_lname:
    print(line, '\n')

# Функциональность itemgetter() иногда может быть заменена lambda выражением.
rows_by_fname_one = sorted(rows, key=lambda r: (r['lname'], r['fname']))
for row in rows_by_fname_one:
    print(row)
