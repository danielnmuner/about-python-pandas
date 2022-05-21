def n_pairs():
    for i in range(1, 201):
        if i%2 == 0:
            yield i 

n_first_pairs = n_pairs()

for i in range(101):
    print((next(n_first_pairs)))