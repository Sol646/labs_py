list_of_vars = [1, 2, 3, 4, 6, 7, 8, 9, None, 0, -7]
missing_index = None  # Индекс пропущенного элемента
NUMBER_OF_NONES = 1  # Кол-во пропусков, указанных в задании
for i in list_of_vars:
    if i is None:
        missing_index = list_of_vars.index(i)
        list_of_vars.remove(None)
        list_of_vars.insert(missing_index, sum(list_of_vars) / (len(list_of_vars) + NUMBER_OF_NONES))
        break

print("Результат:", list_of_vars)
