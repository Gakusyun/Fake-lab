import random

while True:
    try:
        a=int(input('请输入精确到小数点后多少位 '))
    except:
        print('你是不是输错了')
        a=0
    while True:
        if a==0:
            break
        num=[]
        ave=input("输入原始数据（输入Re重置精确到小数点后位数） ")
        if ave in ['re','Re','RE','rE']:
            break
        ave=eval(ave)
        ave*=pow(10,a)
        n=int(input("你想生成数据的个数 "))
        if n%2==1:
            n-=1
            num.append(ave)
        for i in range(n//2):
            temp=random.randint(1,9)
            num.append(ave+temp)
            num.append(ave-temp)
        random.shuffle(num)
        for i in range(n):
            num[random.randint(0,len(num)-1)]+=1
            num[random.randint(0,len(num)-1)]-=1
        for i in num:
            print(i/pow(10,a),end='\t')
        print()