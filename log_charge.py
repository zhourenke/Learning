import time
import log_money

time = time.strftime("(%Y/%m/%d)[%H:%M:%S]")

log = open(".expenses_log.txt", "a")
log.write(time + "花费%.2f元\n" % log_money.charge)
