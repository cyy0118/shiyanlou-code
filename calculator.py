import sys

def calculator(income):
    start_point = 5000  # 起征点
    social_insurance_point = 0.08 + 0.02 + 0.005 + 0.06 # 社保比例
    # 需要缴税的那部分工资
    tax_part = income * (1 - social_insurance_point) - start_point
    if tax_part <= 0:
        tax = 0
    elif tax_part <= 3000:
        tax = tax_part * 0.03
    elif tax_part <= 12000:
        tax = tax_part * 0.1 - 210
    elif tax_part <= 25000:
        tax = tax_part * 0.2 - 1410
    elif tax_part <= 35000:
        tax = tax_part * 0.25 - 2660
    elif tax_part <= 55000:
        tax = tax_part * 0.3 - 4410
    elif tax_part <= 80000:
        tax = tax_part * 0.35 - 7160
    else:
        tax = tax_part * 0.45 - 15160
    salary = income * (1 - social_insurance_point) - tax
    return '{:.2f}'.format(salary)

def main():
    """
    对命令行传入的每一个用户，依次调用计算器计算纳税额
    """
    # 循环处理每一个用户
    for item in sys.argv[1:]:
        # 解析用户 ID 和工资
        id, income = item.split(':')
        try:
            income = int(income)
        except ValueError:
            print('请在薪资的位置输入数字')
            continue
        print('{}:{}'.format(id,calculator(income)))

if __name__ == '__main__':
    main()


