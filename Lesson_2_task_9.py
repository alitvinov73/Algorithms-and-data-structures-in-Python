# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

lPr = True
sumFigureResult = 0
number_Result = 0

while lPr:
    num = input('Введите натуральное число (или 0, если хотите прекратить ввод): ')
    if int(num) == 0:
        break
    currentSumFigure = 0
    for i in num:
        currentSumFigure += int(i)
    if currentSumFigure > sumFigureResult:
        sumFigureResult = currentSumFigure
        number_Result = num

print(f'Число с максимальной суммой цифр: {number_Result}, сумма цифр равна: {sumFigureResult}')
