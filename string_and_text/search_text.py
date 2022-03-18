# Вам нужно проверить начало или конец строки на присутствие неких текстовых
# шаблонов, таких как расширения файлов, схемы URL и т. д

# Простой способ проверить начало или конец строки – применить метод str.
# startswith() или str.endswith().

import os
from urllib.request import urlopen
# files = os.listdir('C:\\Users/phant/OneDrive/Рабочий стол/render_html/python_book_recipe/algoritm.py')
file = 'spam.txt'
print(file.endswith('.txt'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# Если вам нужно проверить несколько вариантов, передайте кортеж с  ними
# в startswith() или endswith():

filenames = os.listdir('.')
a = [name for name in filenames if name.endswith('.py')]


# А вот другой пример
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
