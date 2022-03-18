# Вам нужно манипулировать путями к файлам, чтобы найти имя файла, название
# каталога, абсолютный путь и т. д

import os

path = '~file_recipe/modelu_os_path.py'
print(os.path.expanduser(path))

print(os.path.splitext(path))
# print(os.path.dirname('modelu_os_path.py'))

# Вам нужно выяснить, существует ли файл или каталог.
print(os.path.isdir('file_recipe'))

print(os.path.getsize('modelu_os_path.py'))