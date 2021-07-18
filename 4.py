dict_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('4n.txt', 'w') as nf:
    with open('4.txt', 'r') as mf:
        nf.write(str([line.replace(line.split()[0], dict_rus.get(line.split()[0])) for line in mf]))

