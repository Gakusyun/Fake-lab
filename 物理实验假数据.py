import random


def test(c):
    b = 0
    for j in c:
        if j in ['r', 'R']:
            if b == 0:
                b += 1
        if j in ['e', 'E']:
            b += 1
        if j in ['x', 'X']:
            if b == 1:
                b += 1
        if j in ['i', 'I']:
            if b == 2:
                b += 1
        if j in ['t', 'T']:
            if b == 3:
                b += 1
    return b


back = 0
while True:
    if back == 4:
        break
    a = input('请输入精确到小数点后多少位 ')
    back = 0
    back = test(a)
    if back == 4:
        break
    elif back == 2:
        back = 0
        continue
    try:
        a = int(a)
    except:
        print('你是不是输错了')
        continue
    while True:
        n = input('你想生成数据的个数 ')
        back = test(n)
        if back == 4:
            break
        elif back == 2:
            back = 0
            break
        try:
            n = eval(n)
        except:
            print('你是不是输错了(输入Re重置精确到小数点后位数)')
            continue
        break
    if back == 4:
        continue
    while True:
        num = []
        ave = input("输入Re重置精确到小数点后位数和生成个数\n输入原始数据 ")
        back = test(ave)
        if back == 4:
            break
        elif back == 2:
            back = 0
            break
        try:
            ave = eval(ave)
        except:
            print('你是不是输错了')
            continue
        ave *= pow(10, a)
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
