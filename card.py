import random

card_pool = ("嬴政","诸葛亮","武则天","李白","宫本武藏")
package = []
while 1:
    choose = int(input("""
    充值能让你变得更强！
    请选择指令：
    1.抽卡
    2.查看背包
    3.整理背包
    4.离开
    """))
    if choose == 1:
        number = int(input("输入抽卡次数: "))
        for i in range(0,number):
            n = random.randint(0,4)
            print("你抽到了：{}".format(card_pool[n]))
            package.append(card_pool[n])
        print("卡已存入背包")
        print("____________")

    if choose == 2:
        if len(package) == 0:
            print("背包没有英雄，快去抽卡吧！")
            print("________________")
        else:
            for i in package:
                print(i)
                print("_____________")

    if choose == 3:
        if len(package) == 0:
            print("背包没有英雄，快去抽卡吧!")
            print("__________________")
        else:
            package.sort()
            for i in package:
                print(i)
    if choose == 4:
        break
