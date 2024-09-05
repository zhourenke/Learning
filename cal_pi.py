import math
from decimal import Decimal, getcontext
from concurrent.futures import ThreadPoolExecutor, as_completed


def chudnovsky_term(k):
    """计算 Chudnovsky 公式中的第 k 项"""
    k = Decimal(k)
    getcontext().prec += 2  # 增加临时精度以减少中间计算误差
    numerator = math.factorial(6 * int(k)) * (545140134 * k + 13591409)
    denominator = math.factorial(3 * int(k)) * math.factorial(int(k)) ** 3 * (-262537412640768000) ** int(k)
    term = Decimal(numerator) / Decimal(denominator)
    return term


def compute_pi(target_precision):
    getcontext().prec = target_precision + 10  # 设置全局精度
    C = 426880 * Decimal(math.sqrt(10005))

    terms = 1000  # 可以根据需要调整分割的项数

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(chudnovsky_term, k) for k in range(terms)]

        S = sum(future.result() for future in as_completed(futures))

    pi_value = C / S
    return +pi_value


# 示例使用
target_precision = 10000  # 精度设置为1000位
pi_value = compute_pi(target_precision)
print(f"π with precision of {target_precision} digits:\n{pi_value}")
