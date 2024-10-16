numbers = list(map(int,input("введите числа через пробел:").split()))
#создание нового списка с квадратами чисел
squares = [numbers**2 for number in numbers]
#вывод результата
print(squares)