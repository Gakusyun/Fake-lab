import random
def test(n):
    n = n.upper()
    return n



back = ""
while True:
    if back == "EXIT":
        break
    a = input("请输入精确到小数点后多少位 ")
    back = test(a)
    if back == "EXIT":
        break
    elif back == "RE":
        back = ""
        continue
    try:
        a = int(a)
    except:
        print("你是不是输错了")
        continue
    while True:
        n = input("你想生成数据的个数 ")
        back = test(n)
        if back == "EXIT":
            break
        elif back == "RE":
            back = ""
            break
        try:
            n = eval(n)
            nn = n
        except:
            print("你是不是输错了(输入Reset重置精确到小数点后位数)")
            continue
        break
    if back == "EXIT":
        continue
    while True:
        num = []
        ave = input("输入Reset重置精确到小数点后位数和生成个数\n输入原始数据 ")
        back = test(ave)
        if back == "EXIT":
            break
        elif back == "RE":
            back = ""
            break
        try:
            ave = eval(ave)
        except:
            print("你是不是输错了")
            continue
        ave *= pow(10, a)
        n = nn
        if n % 2 == 1:
            n -= 1
            num.append(ave)
        for i in range(n // 2):
            temp = random.randint(1, 9)
            num.append(ave + temp)
            num.append(ave - temp)
        random.shuffle(num)
        for i in range(n):
            num[random.randint(0, len(num) - 1)] += 1
            num[random.randint(0, len(num) - 1)] -= 1
        for i in num:
            print(i / pow(10, a), end='\t')
        print()
