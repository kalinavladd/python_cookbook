# Вам нужно распаковать N элементов из итерируемого объекта, но этот объект может содержать больше N элементов,
# что вызывает исключение «too many values to
# unpack» («слишком много значений для распаковки»).

# Для решения этой задачи можно использовать «выражения со звездочкой».



def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(name)
print(email)
print(phone)

records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:

    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

items = [1, 10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))