import random
import os


def Accuracy():
    while True:
        Accuracys = input("请输入精确到小数点后位数 ")
        try:
            Accuracys = int(Accuracys)
        except:
            print("你是不是输错了")
            continue
        break
    return Accuracys


def Quantity():
    while True:
        Quantitys = input("请输入需要数据的数量 ")
        try:
            Quantitys = int(Quantitys)
        except:
            print("你是不是输错了")
            continue
        break
    return Quantitys


def Number():
    while True:
        Numbers = input("请输入数据平均值 ")
        try:
            Numbers = float(Numbers)
        except:
            print("你是不是输错了")
            continue
        break
    return Numbers


def spawn(Accuracys, Quantitys, Numbers):
    num = []
    if Quantitys % 2 == 1:
        Quantitys -= 1
        Numbers *= pow(10, Accuracys)
        num.append(Numbers)
    for i in range(Quantitys // 2):
        temp = random.randint(1, 9)
        num.append(Numbers + temp)
        num.append(Numbers - temp)
    random.shuffle(num)
    for i in range(Quantitys):
        num[random.randint(0, len(num) - 1)] += 1
        num[random.randint(0, len(num) - 1)] -= 1
    return num


def printnum(num, Accuracys):
    for i in num:
        print(i / pow(10, Accuracys), end="\t")
        print()
def menu():
    print("1.平均值模式")
    print("2.线性模式")
    print("0. 返回")

def main():
    menu()
    choice =input("请选择:")
    if(choice=="1"):
        Accuracys = Accuracy()
        Quantitys = Quantity()
        while True:
            Numbers = Number()
            num = spawn(Accuracys, Quantitys, Numbers)
            printnum(num, Accuracys)
    elif(choice=="2"):
        print("")#待开发


if __name__ == "__main__":
    main()
