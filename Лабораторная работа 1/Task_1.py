numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
without_none = numbers[:4] + numbers[5:]    # Создание списка без пропущенного элемента
quantity = len(numbers)    # Подсчет количества элементов
s = sum(without_none)
average = s / quantity    # Подсчет среднего арифметического
numbers[4] = average
print("Измененный список:", numbers)