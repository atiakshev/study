# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

list = ['Mercury\n', 'Venus\n', 'Earth\n',
        'Mars\n' 'Jupiter\n', 'Saturn\n',
        'Uranus\n', 'Neptune\n']
with open('solar_system.txt', 'w') as file_obj:
    file_obj.writelines(list)
lines_n = 0
words_n = 0
f = open('solar_system.txt', 'r')
for line in f:
    lines_n += 1
    words = line.split()
    words_n += len(words)
f.close()
print(lines_n)
print(words_n)

