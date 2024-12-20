#обьявление списка
numbers_list = [3, 5, 1, 8, 2]

max= numbers_list[0]  # Начинаем с первого элемента
index = 1  # Индекс для цикла

while index < len(numbers_list):
        if numbers_list[index] > max:
            max = numbers_list[index]  # Обновляем max
        index += 1  # Переходим к следующему элементу

print(f"Максимальное число в списке: {max}")