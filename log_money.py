exp = open(".expenses.txt", "r")
sources = float(exp.read())

charge = float(input("这次吃饭花了多少？\n> "))
changes = charge - 10
result = sources + changes

exp = open(".expenses.txt", "w")
exp.write(f"{result}")
