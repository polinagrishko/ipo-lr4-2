numbers = input("введите значения").split() #получение  списка с клавиатуры
numbers = [int(num) for num in numbers] #конвертирование полученной строки в целочисленный тип данных
for num in numbers: #цикл for для каждого элемента списка
  print(num**2)#вывод значения
