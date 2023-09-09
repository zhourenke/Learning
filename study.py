import head_code

head_code.head()  # 输出占位头

# print("1\r23")
# print("11\t112\t111\t123")  # 转义字符，包括 \t制表 \n换行 \\打印“ \ ” \'打印“ ' ” \"打印“"” \r回车
#
# import multi
#
# print(multi.result)  # 模块中的每一个变量都可以引用

num_list = ["111", "222", "333", "444", "555"]
print(num_list[1])  # 从列表中取值
print(num_list.index("111"))  # 从列表中取索引
num_list[1] = "123"  # 修改列表中的数据
print(num_list)
num_list.append("666")  # 追加数据到列表末尾
print(num_list)
num_list.insert(3, "123")  # 在指定索引处插入一条数据
print(num_list)
num1_list = ["ni hao", "zai ma"]
num_list.extend(num1_list)  # 将列表 num1_list 连接在列表 num_list 后面
print(num_list)
num_list.remove("111")  # 通过字符串搜索从列表中删除指定数据
print(num_list)
num_list.pop(3)  # 通过索引搜索从列表中删除指定数据
print(num_list)
num_list.pop()  # 删除列表中最后一个数据
num_list.clear()  # 清空列表中现有的数据
print(num_list)
