#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']

aList.extend(bList)
print("Extended List:", aList)