import time
import log_money

time = time.strftime("(%Y/%m/%d/%w)[%H:%M:%S]")

log = open(".expenses_log.txt", "a")
log.write(time + "%.2f\n" % log_money.charge)
