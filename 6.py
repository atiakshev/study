subj = {}
with open('6.txt', 'r') as f:
    for line in f:
        subject, stats = line.split(':')
        elems = [i for i in stats if 1 == '' or (i >= '0' and i <= '9')]
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subj[subject] = name_sum
    print(f'{subj}')

