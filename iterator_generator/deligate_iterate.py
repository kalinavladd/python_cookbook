# Вы создали нестандартный объект-контейнер, который внутри содержит список,
# кортеж или какой-то другой итерируемый объект. Вы хотите заставить ваш новый
# контейнер работать с итерациями.

# В типичном случае вам нужно определить метод __iter__(), который делегирует
# итерацию внутреннему содержимому контейнера

class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
