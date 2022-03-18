# Вам нужно разделить строку на поля, но разделители (и пробелы вокруг них)
# внутри строки разные.

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

new_line = re.split(r'[;,\s]\s*', line)
print(new_line)
