# Некий деятель ввел текст «pýtĥöñ» в форму на вашей веб-странице, и вы хотите
# как-то почистить эту строку.
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'

# Первый шаг – удалить пробел. Сделаем небольшую таблицу перевода и задействуем translate():

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Удален
}
print(s)
a = s.translate(remap)
print(a)

# Вы можете продолжить идею и создать намного более крупные таблицы перевода.
# Например, давайте удалим все комбинирующиеся символы:

# cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode))
# if unicodedata.combining(chr(c))
# d = unicodedata.normalize('NFD', a)


# программа для чистки текста (как пример)
def clean_spaces(s) -> str:
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


print('a', 'b', 'c', sep=':')
