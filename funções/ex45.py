def fatorial(x):
    if x == 0:
        return 1
    else:
        return (x * fatorial(x - 1))
y = 4
z = 10
print("O fatorial de {} é {}".format(y, fatorial(y)))
print("O fatorial de {} é {}".format(z, fatorial(z)))