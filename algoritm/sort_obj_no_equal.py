# Вы хотите отсортировать объекты одного класса, но они не поддерживают операции сравнения.
from operator import attrgetter

# Например, если у вас в приложении есть последовательность экземпляров класса User
# и вы хотите отсортировать их по атрибуту user_id, то вы могли бы предоставить
# вызываемый объект, который принимает экземпляр класса User и  возвращает
# атрибут user_id


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]

c = sorted(users, key=lambda u: u.user_id)
print(c)

# Вместо lambda можно применить альтернативный подход с  использованием
# operator.attrgetter():

sort = sorted(users, key=attrgetter('user_id'))
print(sort)
