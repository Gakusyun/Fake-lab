import random

while True:
    a=eval(input("请输入数据精确到小数点后多少位 "))
    while True:
        num=[]
        adv=input("输入原始数据（输入Re重置精确到小数点后位数） ")
        if adv in ['re','Re','RE']:
            break
        adv=eval(adv)
        adv*=pow(10,a)
        n=eval(input("你想生成数据的个数 "))
        if n%2==1:
            n-=1
            num.append(adv)
        for i in range(n//2):
            temp=random.randint(1,9)
            num.append(adv+temp)
            num.append(adv-temp)
        random.shuffle(num)
        for i in range(n//2):
            num[random.randint(0,len(num))]+=1
            num[random.randint(0,len(num))]-=1
        for i in num:
            print(i/pow(10,a),end='\t')
        print()