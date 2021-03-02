import torch

b = torch.zeros((128, 784))
print(b.shape)
size = (1, 28, 28)

"""
*号的作用是分配元组中的数据
"""
c = b.view(-1, *size)
print(f"c.shape = {c.shape}") #torch.Size([128, 1, 28, 28])

#上面*size的作用就是将（1， 28，28）转换为1，28， 28
#因此上面的这句话的作用类似与b.view(-1, 1, 28, 28)
d = b.view(-1, 1, 28, 28)
print(f"d.shape={d.shape}")

def fun(*size): #*代表收集参数,作用是将调用时提供的所有值，放在一个元组里。
    print(type(size)) # 这个时候size的类型是<class 'tuple'>
    print(size) # 内容为元组内容(1, 2, 3)
    print(*size) #内容为 1 2 3
fun(1, 2, 3) #1 2 3

