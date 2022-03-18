from collections import defaultdict
#
# d = {
#     'a': [1, 2, 3],
#     'b': [4, 5]
# }
#Вы хотите создать словарь, который отображает ключи на более
# чем одно значение (так называемый «мультисловарь», multidict).
# e = {
#     'a': {1, 2, 3},
#     'b': {4, 5}
# }

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)


q = defaultdict(set)
q['a'].add(1)
q['a'].add(2)
q['a'].add(4)

a = {}
a.setdefault('a', [].append(1))
a.setdefault('a', [].append(2))
a.setdefault('a', [].append(3))
print(a)
