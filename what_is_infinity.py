n = 1
e = 0
while e < 2.718281828459045:
    n = 2 * n
    e = (1 + 1/n) ** n
print(n)

n = 4503599627370498
e = (1 + 1/n) ** n
print(e)
