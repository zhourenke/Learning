#!/bin/python

exp = open(".expenses.txt", "r")
sources = float(exp.read())
exp.close()
charge_money = float(input("这次吃饭花了多少？\n> "))
changes = charge_money - 10
result = sources + changes
exp = open(".expenses.txt", "w")
exp.write(f"{result}")
exp.close()
if result > 0:
    print("还要省%.2f元，继续加油" % result)
else:
    result = 0 - result
    print("攒了%.2f元零花钱，可以买写小玩意了！\n好耶 :D" % result)
