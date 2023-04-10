import random

while True:
    精确位数=eval(input("请输入数据精确到小数点后多少位"))
    while True:
        num=[]
        平均数=eval(input("输入原始数据"))
        平均数*=pow(10,精确位数)
        个数=eval(input("你想生成数据的个数"))
        if 个数%2==1:
            个数-=1
            num.append(平均数)
        个数//=2
        for i in range(个数):
            临时=random.randint(1,9)
            num.append(平均数+临时)
            num.append(平均数-临时)
        random.shuffle(num)
        for i in num:
            print(i/pow(10,精确位数),end='\t')