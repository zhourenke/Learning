import head_code

head_code.head()  # 输出占位头

# print("1\r23")
# print("11\t112\t111\t123")  # 转义字符，包括 \t制表 \n换行 \\打印“ \ ” \'打印“ ' ” \"打印“"” \r回车
#
# import multi
#
# print(multi.result)  # 模块中的每一个变量都可以引用

str_list = ["ni hao", "zai ma", "zai jian"]
int_list = [1, 2, 234, 654, 4]
str_list.sort(key=len)  # 以 key 中参数的方式排序
int_list.sort(reverse=True)  # 反转排序顺序
print(str_list)
print(int_list)
