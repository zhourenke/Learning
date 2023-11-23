import log_money
import log_charge

if log_money.result > 0:
    print("还要省%.2f元，继续加油" % log_money.result)
else:
    result = 0 - log_money.result
    print("攒了%.2f元零花钱，可以买些小玩意了！\n好耶 :D" % result)
