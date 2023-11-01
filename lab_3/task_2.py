def find_common_participants(first_group, second_group, arg=','):
    set_participants = set(first_group.split(arg)).intersection(second_group.split(arg))
    return sorted(list(set_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, arg='|')
