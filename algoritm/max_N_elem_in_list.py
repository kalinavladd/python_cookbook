#  У вас есть последовательность элементов, и вы хотите узнать, какие элементы
# встречаются в ней чаще всего.

# Класс collections.Counter разработан как раз для решения подобных задач. В нем
# даже есть удобный метод most_common(), который сразу выдаст вам ответ.

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under',
]

word_count = Counter(words)

top_three = word_count.most_common(3)
print(top_three)

# можно с ними проводить математические операции
morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a + b
print(c)

