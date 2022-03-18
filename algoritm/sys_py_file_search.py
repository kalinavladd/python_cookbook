import os

# Определяем, есть ли файлы .py в каталоге
files = os.listdir('C:\\Users/phant/OneDrive/Рабочий стол/render_html/python_book_recipe/algoritm')

if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry')

# Выводит кортеж как CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

