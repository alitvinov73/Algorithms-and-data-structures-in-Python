# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа
# должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о
# возможности деления на ноль, если он ввел его в качестве делителя.
lPr = True

def operate(myValue, oper):
    if len(myValue) == 3 and (myValue[0].strip().isdigit() and myValue[2].strip().isdigit()):
        if oper == '+':
            print(f'Выражение {myValue[0]} {oper} {myValue[2]} = {float(myValue[0]) + float(myValue[2])}')
        elif oper == '-':
            print(f'Выражение {myValue[0]} {oper} {myValue[2]} = {float(myValue[0]) - float(myValue[2])}')
        elif oper == '*':
            print(f'Выражение {myValue[0]} {oper} {myValue[2]} = {float(myValue[0]) * float(myValue[2])}')
        elif oper == '/':
            print(f'Выражение {myValue[0]} {oper} {myValue[2]} = {float(myValue[0]) / float(myValue[2])}')
    else:
        print('Введено не корректное выражение, попробуйте еще.')


print("Введите математическое выражение из двух чисел и операнда между ними ( '+', '-', '', '/').\n"
      "перед и после операнда пробел обязателен. "
      "При вводе '0' в качестве операнда, вычисления завершаются.\n")
while lPr:
    myValue = input("Введите выражение: ")
    if myValue.find(' + ') != -1:
        operate(myValue.split(), '+')
    elif myValue.find(' - ') != -1:
        operate(myValue.split(), '-')
    elif myValue.find(' * ') != -1:
        operate(myValue.split(), '*')
    elif myValue.find(' / ') != -1:
        operate(myValue.split(), '/')
    elif myValue.find(' 0 ') != -1:
        print('Вычисления окончены.')
        lPr = False
    else:
        print('Введено не корректное выражение, попробуйте еще.')
