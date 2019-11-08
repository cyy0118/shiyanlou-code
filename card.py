import random

kc = ("宫本武藏","李白","武则天","诸葛亮","嬴政")
bb = []
while 1:
    zjm = int(input('''
    充值能让你变得更强！
    请选择指令:
    1.抽卡
    2.查看背包
    3.整理背包
    4.离开
    '''))
    if zjm == 1:
        ck = int(input("输入抽卡次数:"))
        for i in range(0,ck):
            n = random.randint(0,4)
            print("你抽到了:{}".format(kc[n]))
            bb.append(kc[n])

        print("卡已存到背包")
        print("______________")

    if zjm == 2:
        if len(bb) == 0:
            print("背包暂无英雄，快去抽卡吧！")
            print("________________________")
        else:
            for i in bb:
                print(i)
            print("__________")

    if zjm == 3:
        if len(bb) == 0:
            print("背包暂无英雄，快去抽卡吧！")
            print("___________")
        else:
            bb.sort()
            for i in bb:
                print(i)
            print("__________")

    if zjm == 4:
        break
