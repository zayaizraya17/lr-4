#Ввод значений с клавиатуры
number_input=int(input("Введите значение для вывода всех четных чисел от 0 до n-числа"))
#генератор списка
print([i for i in range(0,number_input,2)])