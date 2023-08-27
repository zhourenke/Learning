import head_code

head_code.head()  # 输出占位头

# print("1\r23")
# print("11\t112\t111\t123")  # 转义字符，包括 \t制表 \n换行 \\打印“ \ ” \'打印“ ' ” \"打印“"” \r回车


def multi(num1, num2):
    # 求积
    return num1 * num2  # 将计算结果返回，进而在def以外调用


print(multi(1, 2))
