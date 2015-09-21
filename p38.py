import itertools

pandigital = '987654321'
perms = itertools.permutations(pandigital)

for n in range(1, 10**10):
    cur_perm = pandigital
    c = 1
    while len(cur_perm) > 0 and str(n * c) in cur_perm:
        cur_perm = cur_perm.replace(str(n * c), '')
        c = c + 1
    if len(cur_perm) <= 0:
        print('Found it!', n, c - 1)